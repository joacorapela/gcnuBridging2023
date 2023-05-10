
"""
Batch Bayesian linear regression
================================

The code below uses a batch algorithm to estimate the posterior of the weighs
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
likelihood_precision_coef = (1/0.2)**2
data_filename_pattern = "data/linearRegression_nSamples{:02d}.npz"
fig_filename_pattern = "figures/batchBayesianLinearRegression_nSamples{:02d}.{:s}"

#%%
# Load data
# ---------

data_filename = data_filename_pattern.format(n_samples)
load_res = np.load(data_filename)
independent_var = load_res["x"]
dependent_var = load_res["t"]
a0 = load_res["a0"]
a1 = load_res["a1"]

#%%
# Estimate posterior
# ------------------

Phi = np.column_stack((np.ones(len(independent_var)), independent_var))
alpha = prior_precision_coef
beta = likelihood_precision_coef
mN, SN = \
    joacorapela_common.stats.bayesianLinearRegression.batchWithSimplePrior(
        Phi=Phi, y=dependent_var, alpha=alpha, beta=beta)

#%%
# Plot the estimates
# ------------------
marker_true = "cross"
size_true = 10
color_true = "white"
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

rv = scipy.stats.multivariate_normal(mN, SN)
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

png_fig_filename = fig_filename_pattern.format(n_samples, "png")
html_fig_filename = fig_filename_pattern.format(n_samples, "html")
fig.write_image(png_fig_filename)
fig.write_html(html_fig_filename)

fig

