
"""
Online Bayesian linear regression
================================

The code below uses an online algorithm to estimate the posterior of the weighs
of a linear regression model using simulate data.

"""

#%%
# Import requirments
# ------------------

import numpy as np
import scipy.stats
import plotly.graph_objects as go

import joacorapela_common.stats.bayesianLinearRegression

#%%
# Define data generation variables
# --------------------------------

n_samples = 20
prior_precision_coef = 2.0
data_filename_pattern = "data/linearRegression_nSamples{:02d}.npz"
like_fig_filename_pattern = ("figures/onlineBayesianLinearRegression_"
                             "likelihood_sample{:02d}_nSamples{:02d}.{:s}")
post_fig_filename_pattern = ("figures/onlineBayesianLinearRegression_"
                             "posterior_sample{:02d}_nSamples{:02d}.{:s}")

#%%
# Load data
# ---------

data_filename = data_filename_pattern.format(n_samples)
load_res = np.load(data_filename)
independent_var = load_res["x"]
noiseless_dependent_var = load_res["y"]
dependent_var = load_res["t"]
a0 = load_res["a0"]
a1 = load_res["a1"]
sigma = load_res["sigma"]
likelihood_precision_coef = (1.0/sigma)**2

#%%
# Estimate and plot posterior
# ---------------------------

marker_true = "cross"
size_true = 10
color_true = "white"
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

Phi = np.column_stack((np.ones(len(independent_var)), independent_var))
alpha = prior_precision_coef
beta = likelihood_precision_coef

# set prior
m0 = np.array([0.0, 0.0])
S0 = 1.0 / alpha * np.eye(2)
#

mn = m0
Sn = S0
for n, t in enumerate(dependent_var):
    print(f"Processing {n}/({len(dependent_var)})")
    # compute likelihood
    Z = np.empty(shape=(len(x), len(y)), dtype=np.double)
    for i, w0 in enumerate(x):
        for j, w1 in enumerate(y):
            rv = scipy.stats.norm(w0 + w1 * independent_var[n], sigma)
            Z[j, i] = rv.pdf(t)

    # plot likelihood
    fig = go.Figure()
    trace_post = go.Contour(x=x, y=y, z=Z, showscale=False)
    fig.add_trace(trace_post)
    trace_true_coef = go.Scatter(x=[a0], y=[a1], mode="markers",
                                 marker_symbol=marker_true,
                                 marker_size=size_true,
                                 marker_color=color_true,
                                 name="true mean")
    fig.add_trace(trace_true_coef)
    fig.update_layout(xaxis_title="Intercept",
                      yaxis_title="Slope")
    png_fig_filename = like_fig_filename_pattern.format(n, n_samples, "png")
    html_fig_filename = like_fig_filename_pattern.format(n, n_samples, "html")
    fig.write_image(png_fig_filename)
    fig.write_html(html_fig_filename)

    # update posterior
    mn, Sn = joacorapela_common.stats.bayesianLinearRegression.onlineUpdate(
        mn=mn, Sn=Sn, phi=Phi[n, :], y=t, alpha=alpha, beta=beta)

    # plot updated posterior
    rv = scipy.stats.multivariate_normal(mn, Sn)
    Z = rv.pdf(pos)
    fig = go.Figure()
    trace_post = go.Contour(x=x, y=y, z=Z, showscale=False)
    fig.add_trace(trace_post)
    trace_true_coef = go.Scatter(x=[a0], y=[a1], mode="markers",
                                 marker_symbol=marker_true,
                                 marker_size=size_true,
                                 marker_color=color_true,
                                 name="true mean")
    fig.add_trace(trace_true_coef)
    fig.update_layout(xaxis_title="Intercept",
                      yaxis_title="Slope")
    png_fig_filename = post_fig_filename_pattern.format(n, n_samples, "png")
    html_fig_filename = post_fig_filename_pattern.format(n, n_samples, "html")
    fig.write_image(png_fig_filename)
    fig.write_html(html_fig_filename)

fig.show()

breakpoint()
