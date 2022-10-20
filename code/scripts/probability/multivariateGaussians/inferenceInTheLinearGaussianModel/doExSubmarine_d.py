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
    parser.add_argument("--y_info_filename_pattern",
                        help="pattern of filename to save samples, mean and "
                        "covariance of y", type=str,
                        default="results/y_info_nSamples{:05d}.npz")
    parser.add_argument("--y_metadata_filename_pattern",
                        help="pattern of filename to save metadata of y",
                        type=str,
                        default="results/y_metadata_nSamples{:05d}.ini")
    args = parser.parse_args()

    n_samples = args.n_samples
    n_points_ellipse = args.n_points_ellipse
    ellipse_quantile = args.ellipse_quantile
    y_info_filename = args.y_info_filename_pattern.format(n_samples)
    y_metadata_filename = args.y_metadata_filename_pattern.format(n_samples)

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
    pos_mean_z = np.linalg.solve(tmp1, tmp2)
    pos_cov_z = np.linalg.inv(tmp1)

    ellipse_x, ellipse_y = \
        joacorapela_common.utils.probability.quantileEllipse(
            mean=pos_mean_z, cov=pos_cov_z, quantile=ellipse_quantile,
            N=n_points_ellipse)

    # plot data
    fig = go.Figure()
    trace_z = go.Scatter(x=[z[0]], y=[z[1]], mode="markers", name="z")
    trace_mean = go.Scatter(x=[pos_mean_z[0]], y=[pos_mean_z[1]],
                            mode="markers", name="posterior mean")
    trace_ellipse = go.Scatter(x=ellipse_x, y=ellipse_y, mode="lines",
                               name="{:.0f}% quantile".format(
                                   ellipse_quantile*100))
    trace_yBar = go.Scatter(x=[sample_mean_y[0]], y=[sample_mean_y[1]],
                            mode="markers", name=r"$\bar{y}$")
    fig.add_trace(trace_z)
    fig.add_trace(trace_mean)
    fig.add_trace(trace_ellipse)
    fig.add_trace(trace_yBar)
    fig.update_layout(
        xaxis_title="x",
        yaxis_title="y",
        yaxis=dict(scaleanchor="x", scaleratio=1),
    )

    fig.show()

    import pdb; pdb.set_trace()


if __name__ == "__main__":
    main(sys.argv)
