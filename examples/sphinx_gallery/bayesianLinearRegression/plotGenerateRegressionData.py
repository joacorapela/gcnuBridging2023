
"""
Data generation script for Bayesian linear regression
=====================================================

The code below generates data for Bayesian linear regression.

"""

#%%
# Import requirments
# ------------------

import numpy as np
import plotly.graph_objects as go

#%%
# Define data generation variables
# --------------------------------

n_samples = 20
a0    = -0.3
a1    = 0.5
sigma = 0.2
data_filename_pattern = "data/linearRegression_nSamples{:02d}.npz"
fig_filename_pattern = "figures/regression_data_nSamples{:02d}.{:s}"

#%%
# Sample data
# -----------

x = np.random.uniform(low=-1, high=1, size=n_samples)
y = a0 + a1 * x
t = y + np.random.standard_normal(size=y.shape) * sigma

#%%
# Save data
# ---------

data_filename = data_filename_pattern.format(n_samples)
np.savez(data_filename, x=x, y=y, t=t, a0=a0, a1=a1, sigma=sigma)

#%%
# Plot data
# -----------

fig = go.Figure()
trace_y = go.Scatter(x=x, y=y, mode="lines+markers", name="true reaction times")
fig.add_trace(trace_y)
trace_t = go.Scatter(x=x, y=t, mode="markers", name="noisy reaction times")
fig.add_trace(trace_t)
fig.update_xaxes(title_text="Grating Contrast")
fig.update_yaxes(title_text="Reaction Time")

png_fig_filename = fig_filename_pattern.format(n_samples, "png")
html_fig_filename = fig_filename_pattern.format(n_samples, "html")
fig.write_image(png_fig_filename)
fig.write_html(html_fig_filename)

fig
