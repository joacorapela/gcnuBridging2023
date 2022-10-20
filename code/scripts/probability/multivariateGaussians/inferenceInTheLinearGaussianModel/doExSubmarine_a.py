import sys
import os.path
import argparse
import numpy as np
import plotly.graph_objects as go

sys.path.append(os.path.expanduser("~/dev/research/programs/repos/python"))
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
    parser.add_argument("--sigma_zx",
                        help="submarine location standard deviation along the "
                             "x axis", type=float, default=1.0)
    parser.add_argument("--sigma_zy",
                        help="submarine location standard deviation along the "
                             "y axis", type=float, default=2.0)
    parser.add_argument("--rho_z",
                        help="submarine location correlation coefficient",
                        type=float, default=0.7)
    parser.add_argument("--z_info_filename", help="filename to save samples, "
                        "mean and covariance of z", type=str,
                        default="results/z_info.npz")
    args = parser.parse_args()

    n_samples = args.n_samples
    n_points_ellipse = args.n_points_ellipse
    ellipse_quantile = args.ellipse_quantile
    mean_z = np.fromstring(args.mean_z, dtype=float, sep=" ")
    sigma_zx = args.sigma_zx
    sigma_zy = args.sigma_zy
    rho_z = args.rho_z
    z_info_filename = args.z_info_filename

    cov_z = np.array([[sigma_zx**2, rho_z*sigma_zx*sigma_zy],
                      [rho_z*sigma_zx*sigma_zy, sigma_zy**2]])
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
                               mode="markers", name="samples")
    trace_mean = go.Scatter(x=[mean_z[0]], y=[mean_z[1]], mode="markers",
                            name="mean")
    trace_ellipse = go.Scatter(x=ellipse_x, y=ellipse_y, mode="lines",
                               name="{:.0f}% quantile".format(
                                   ellipse_quantile*100))
    fig.add_trace(trace_samples)
    fig.add_trace(trace_mean)
    fig.add_trace(trace_ellipse)
    fig.update_layout(
        xaxis_title=r"$z_x$",
        yaxis_title=r"$z_y$",
        yaxis=dict(scaleanchor="x", scaleratio=1),
    )
    fig.show()

    import pdb; pdb.set_trace()


if __name__ == "__main__":
    main(sys.argv)
