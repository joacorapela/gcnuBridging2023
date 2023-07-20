import sys
import os.path
import argparse
import numpy as np
import plotly.graph_objects as go

import joacorapela_common.utils.probability


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_samples",
                        help="number of samples to generate", type=int,
                        default=100)
    parser.add_argument("--n_points_ellipse",
                        help="number of points to use in drawing the "
                             "confidence ellipse", type=int, default=100)
    parser.add_argument("--ellipse_quantile",
                        help="percentage of samples included in the ellipse",
                        type=float, default=0.95)
    parser.add_argument("--mean_z",
                        help="submarine location mean",
                        type=str, default="2.0 3.0")
    parser.add_argument("--color_submarine",
                        help="color of submarine samples",
                        type=str, default="rgba(255, 0, 0, 1.0)")
    parser.add_argument("--marker_mean",
                        help="marker for mean",
                        type=str, default="x")
    parser.add_argument("--marker_samples",
                        help="marker for samples",
                        type=str, default="circle")
    parser.add_argument("--size_mean",
                        help="size for mean",
                        type=int, default=15)
    parser.add_argument("--size_samples",
                        help="size for samples",
                        type=int, default=5)
    parser.add_argument("--z_info_filename", help="filename to save samples, "
                        "mean and covariance of z", type=str,
                        default="results/z_info.npz")
    parser.add_argument("--fig_filename_pattern",
                        help="figure filename pattern",
                        type=str, default="figures/submarine_samples_N{:d}.{:s}")
    args = parser.parse_args()

    n_samples = args.n_samples
    n_points_ellipse = args.n_points_ellipse
    ellipse_quantile = args.ellipse_quantile
    mean_z = np.fromstring(args.mean_z, dtype=float, sep=" ")
    color_submarine = args.color_submarine
    marker_mean = args.marker_mean
    marker_samples = args.marker_samples
    size_mean = args.size_mean
    size_samples = args.size_samples
    z_info_filename = args.z_info_filename
    fig_filename_pattern = args.fig_filename_pattern

    # Please replace x.xx by appropriate values based on the exercise
    # description
    sigma_z_x = 1.00
    sigma_z_y = 1.00
    rho_z = 0.3
    cov_z_11 = 1.0
    cov_z_12 = 0.0
    cov_z_21 = 0.0
    cov_z_22 = 2.0
    #

    cov_z = np.array([[cov_z_11, cov_z_12],
                      [cov_z_21, cov_z_22]])
    samples_z = np.random.multivariate_normal(mean=mean_z, cov=cov_z,
                                              size=n_samples)
    ellipse_x, ellipse_y = \
        joacorapela_common.utils.probability.quantileEllipse(
            mean=mean_z, cov=cov_z, quantile=ellipse_quantile,
            N=n_points_ellipse)

    # save z info for next item
    np.savez(samples_z=samples_z, mean_z=mean_z, cov_z=cov_z,
             file=z_info_filename)

    # plot data
    fig = go.Figure()
    trace_samples = go.Scatter(x=samples_z[:, 0], y=samples_z[:, 1],
                               mode="markers",
                               marker_symbol=marker_samples,
                               marker_size=size_samples,
                               marker_color=color_submarine,
                               name="samples")
    trace_mean = go.Scatter(x=[mean_z[0]], y=[mean_z[1]], mode="markers",
                            marker_symbol=marker_mean,
                            marker_size=size_mean,
                            marker_color=color_submarine,
                            name="mean")
    trace_ellipse = go.Scatter(x=ellipse_x, y=ellipse_y, mode="lines",
                               marker_color=color_submarine,
                               name="{:.0f}% range ellipse".format(
                                   ellipse_quantile*100))
    fig.add_trace(trace_samples)
    fig.add_trace(trace_mean)
    fig.add_trace(trace_ellipse)
    fig.update_layout(
        xaxis_title=r"$z_x$",
        yaxis_title=r"$z_y$",
        yaxis={"scaleanchor": "x", "scaleratio": 1},
        font={"size": 18},
    )
    fig.show()

    png_fig_filename = fig_filename_pattern.format(n_samples, "png")
    html_fig_filename = fig_filename_pattern.format(n_samples, "html")
    fig.write_image(png_fig_filename)
    fig.write_html(html_fig_filename)

    import pdb; pdb.set_trace()


if __name__ == "__main__":
    main(sys.argv)
