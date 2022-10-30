import sys
import os.path
import argparse
import configparser
import numpy as np
import plotly.graph_objects as go

sys.path.append(os.path.expanduser("~/dev/research/programs/repos/python"))
import joacorapela_common.utils.probability


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_samples",
                        help="number of samples to generate", type=int,
                        default=5)
    parser.add_argument("--n_points_ellipse",
                        help="number of points to use in drawing the "
                             "confidence ellipse", type=int, default=100)
    parser.add_argument("--ellipse_quantile",
                        help="percentage of samples included in the ellipse",
                        type=float, default=0.95)
    parser.add_argument("--sigma_y_x",
                        help="measurements noise standard deviation along the "
                             "x axis", type=float, default=1.0)
    parser.add_argument("--sigma_y_y",
                        help="measurements noise standard deviation along the "
                             "y axis", type=float, default=1.0)
    parser.add_argument("--rho_y",
                        help="measurements noise correlation coefficient",
                        type=float, default=0.0)
    parser.add_argument("--color_submarine",
                        help="color of submarine samples",
                        type=str, default="rgba(255, 0, 0, 1.0)")
    parser.add_argument("--color_measurements",
                        help="color of measurement samples",
                        type=str, default="rgba(0, 0, 255, 1.0)")
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
    parser.add_argument("--y_info_filename_pattern", help="pattern of filename "
                        "to save samples, mean and covariance of y", type=str,
                        default="results/y_info_nSamples{:05d}.npz")
    parser.add_argument("--y_metadata_filename_pattern",
                        help="pattern of filename to save metadata of y",
                        type=str, default="results/y_metadata_nSamples{:05d}.ini")
    parser.add_argument("--fig_filename_pattern",
                        help="figure filename pattern",
                        type=str, default="figures/measurements_samples_N{:d}.{:s}")
    args = parser.parse_args()

    n_samples = args.n_samples
    n_points_ellipse = args.n_points_ellipse
    ellipse_quantile = args.ellipse_quantile
    color_submarine = args.color_submarine
    color_measurements = args.color_measurements
    marker_mean = args.marker_mean
    marker_samples = args.marker_samples
    size_mean = args.size_mean
    size_samples = args.size_samples
    z_info_filename = args.z_info_filename
    y_info_filename = args.y_info_filename_pattern.format(n_samples)
    y_metadata_filename = args.y_metadata_filename_pattern.format(n_samples)
    fig_filename_pattern = args.fig_filename_pattern

    # Please replace x.xx by appropriate values based on the exercise
    # description
    sigma_y_x = 1.0
    sigma_y_y = 1.0
    rho_y = 0.0
    cov_y_11 = sigma_y_x**2
    cov_y_12 = rho_y*sigma_y_x*sigma_y_y
    cov_y_21 = rho_y*sigma_y_x*sigma_y_y
    cov_y_22 = sigma_y_y**2
    #
    cov_y = np.array([[cov_y_11, cov_y_12],
                      [cov_y_21, cov_y_22]])

    load_res = np.load(z_info_filename)
    samples_z = load_res["samples_z"]
    mean_y = samples_z[0, :]
    samples_y = np.random.multivariate_normal(mean=mean_y, cov=cov_y,
                                              size=n_samples)

    # save y_info and metadata for next item
    np.savez(samples_y=samples_y, mean_y=mean_y, cov_y=cov_y,
             file=y_info_filename)
    metadata_config = configparser.ConfigParser()
    metadata_config["z_info"] = {"filename": z_info_filename}
    with open(y_metadata_filename, "w") as f:
        metadata_config.write(f)

    ellipse_x, ellipse_y = \
        joacorapela_common.utils.probability.quantileEllipse(
            mean=mean_y, cov=cov_y, quantile=ellipse_quantile,
            N=n_points_ellipse)

    # plot data
    fig = go.Figure()
    trace_samples = go.Scatter(x=samples_y[:, 0], y=samples_y[:, 1],
                               mode="markers",
                               marker_symbol=marker_samples,
                               marker_size=size_samples,
                               marker_color=color_measurements,
                               name="samples")
    trace_mean = go.Scatter(x=[mean_y[0]], y=[mean_y[1]], mode="markers",
                               marker_symbol=marker_mean,
                               marker_size=size_mean,
                               marker_color=color_submarine,
                            name="mean")
    trace_ellipse = go.Scatter(x=ellipse_x, y=ellipse_y, mode="lines",
                               marker_color=color_measurements,
                               name="{:.0f}% CE".format(
                                   ellipse_quantile*100))
    fig.add_trace(trace_samples)
    fig.add_trace(trace_mean)
    fig.add_trace(trace_ellipse)
    fig.update_layout(
        xaxis_title=r"$y_x$",
        yaxis_title=r"$y_y$",
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
