import sys
import os.path
import argparse
import configparser
import numpy as np
import plotly.graph_objects as go

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
    parser.add_argument("--color_submarine",
                        help="color of submarine samples",
                        type=str, default="rgba(255, 0, 0, 1.0)")
    parser.add_argument("--color_measurements",
                        help="color of measurement samples",
                        type=str, default="rgba(0, 0, 255, 1.0)")
    parser.add_argument("--color_posterior",
                        help="color of posterior mean and PE",
                        type=str, default="rgba(255, 165, 0, 1.0)")
    parser.add_argument("--color_sample_mean",
                        help="color of sample mean and its PE",
                        type=str, default="rgba(0, 255, 0, 1.0)")
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
    parser.add_argument("--ylim",
                        help="y-axes limits",
                        type=str, default="[0.0, 4.5]")
    parser.add_argument("--y_info_filename_pattern",
                        help="pattern of filename to save samples, mean and "
                        "covariance of y", type=str,
                        default="results/y_info_nSamples{:05d}.npz")
    parser.add_argument("--y_metadata_filename_pattern",
                        help="pattern of filename to save metadata of y",
                        type=str,
                        default="results/y_metadata_nSamples{:05d}.ini")
    parser.add_argument("--fig_filename_pattern",
                        help="figure filename pattern",
                        type=str, default="figures/estimates_samples_N{:d}.{:s}")
    args = parser.parse_args()

    n_samples = args.n_samples
    n_points_ellipse = args.n_points_ellipse
    ellipse_quantile = args.ellipse_quantile
    color_submarine = args.color_submarine
    color_measurements = args.color_measurements
    color_posterior = args.color_posterior
    color_sample_mean = args.color_sample_mean
    marker_mean = args.marker_mean
    marker_samples = args.marker_samples
    size_mean = args.size_mean
    size_samples = args.size_samples
    ylim = [float(str) for str in args.ylim[1:-1].split(",")]
    y_info_filename = args.y_info_filename_pattern.format(n_samples)
    y_metadata_filename = args.y_metadata_filename_pattern.format(n_samples)
    fig_filename_pattern = args.fig_filename_pattern

    y_info = np.load(y_info_filename)
    samples_y = y_info["samples_y"]
    z = y_info["mean_y"]
    cov_y = y_info["cov_y"]
    N = len(samples_y)
    sample_mean_y = samples_y.mean(axis=0)

    y_metadata = configparser.ConfigParser()
    y_metadata.read(y_metadata_filename)
    z_info_filename = y_metadata["z_info"]["filename"]
    z_info = np.load(z_info_filename)
    mean_z = z_info["mean_z"]
    cov_z = z_info["cov_z"]

    cov_y_inv = np.linalg.inv(cov_y)
    cov_z_inv = np.linalg.inv(cov_z)
    tmp1 = N * cov_y_inv + cov_z_inv
    tmp2 = N * np.matmul(cov_y_inv, sample_mean_y) + \
        np.matmul(cov_z_inv, mean_z)
    post_mean_z = np.linalg.solve(tmp1, tmp2)
    post_cov_z = np.linalg.inv(tmp1)
    yBar_mean = z
    yBar_cov = 1.0/N*cov_y
    #

    post_ellipse_x, post_ellipse_y = \
        joacorapela_common.utils.probability.quantileEllipse(
            mean=post_mean_z, cov=post_cov_z, quantile=ellipse_quantile,
            N=n_points_ellipse)
    yBar_ellipse_x, yBar_ellipse_y = \
        joacorapela_common.utils.probability.quantileEllipse(
            mean=yBar_mean, cov=yBar_cov, quantile=ellipse_quantile,
            N=n_points_ellipse)

    # plot data
    fig = go.Figure()
    trace_z = go.Scatter(x=[z[0]], y=[z[1]], mode="markers",
                         marker_symbol=marker_samples,
                         marker_size=size_samples,
                         marker_color=color_submarine,
                         name=r"$\text{submarine location}\ \mathbf{z}_1$")
    trace_mean = go.Scatter(x=[post_mean_z[0]], y=[post_mean_z[1]],
                            mode="markers",
                            marker_symbol=marker_mean,
                            marker_size=size_mean,
                            marker_color=color_posterior,
                            name=r"posterior mean")
    trace_post_ellipse = go.Scatter(x=post_ellipse_x, y=post_ellipse_y,
                                    mode="lines", marker_color=color_posterior,
                                    name="{:.0f}% posterior sample PE".format(
                                        ellipse_quantile*100))
    trace_yBar = go.Scatter(x=[sample_mean_y[0]], y=[sample_mean_y[1]],
                            mode="markers",
                            marker_symbol=marker_mean,
                            marker_size=size_mean,
                            marker_color=color_sample_mean,
                            name="sample mean")
    trace_yBar_ellipse = go.Scatter(x=yBar_ellipse_x, y=yBar_ellipse_y,
                                    mode="lines",
                                    marker_color=color_sample_mean,
                                    name="95% sample mean PE"
                                   )
    fig.add_trace(trace_z)
    fig.add_trace(trace_mean)
    fig.add_trace(trace_post_ellipse)
    fig.add_trace(trace_yBar)
    fig.add_trace(trace_yBar_ellipse)
    fig.update_layout(
        xaxis_title="x",
        yaxis_title="y",
        yaxis={"scaleanchor": "x", "scaleratio": 1, "range": (0, 5.5),
               "dtick": 1.0},
        xaxis={"range": (0, 5.5), "dtick": 1.0},
        font={"size": 18},
    )

    fig.show()

    png_fig_filename = fig_filename_pattern.format(n_samples, "png")
    html_fig_filename = fig_filename_pattern.format(n_samples, "html")
    fig.write_image(png_fig_filename)
    fig.write_html(html_fig_filename)


if __name__ == "__main__":
    main(sys.argv)
