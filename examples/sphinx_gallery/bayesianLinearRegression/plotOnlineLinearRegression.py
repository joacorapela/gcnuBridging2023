
"""
Oliner Bayesian linear regression
=================================

The code below estimates the posterior of the weighs of a linear regression
model using simulate data.

"""

#%%
# Import requirments
# ------------------

import numpy as np
import scipy.stats
import plotly.graph_objects as go

#%%
# Define data generation variables
# --------------------------------

n_samples = 64
prior_precision_coef = 2.0
likelihood_precision_coef = (1/0.2)**2
data_filename_pattern = "data/linearRegression_nSamples{:02d}.npz"
fig_filename_pattern = "figures/regression_data_nSamples{:02d}.{:s}"

#%%
# Load data
# ---------

data_filename = data_filename_pattern.format(n_samples)
load_res = np.load(data_filename)
x = load_res["x"]
t = load_res["t"]
a0 = load_res["a0"]
a1 = load_res["a1"]

#%%
# Estimate posterior
# ------------------

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

likelihoods = np.empty(size=(len(x), len(y), n_samples+1), dtype=np.double)
posteriors = np.empty(size=(len(x), len(y), n_samples+1), dtype=np.double)

m0 = np.array([0.0, 0.0])
S0 = np.eyes(2)/prior_precision_coef

rv = scipy.stats.multivariate_normal(m0, S0)
posterior = rv.pdf(pos)

for an
alpha = prior_precision_coef
beta = likelihood_precision_coef
Phi = np.column_stack((np.ones(len(x)), x))
SNinv = alpha*np.eye(2) + beta * Phi.T @ Phi
mN = np.linalg.solve(a=SNinv, b=beta * Phi.T @ t)

#%%
# Plot the estimates
# ------------------
ellipse_quantile = .95
n_points_ellipse = 100
marker_true = "cross"
marker_post = "circle"
size_true = 10
size_post = 10
color_true = "white"
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

SN = np.linalg.inv(SNinv)
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

fig.show()

breakpoint()
