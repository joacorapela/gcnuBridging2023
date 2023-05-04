
import numpy as np
import plotly.graph_objects as go

N     = 20
a0    = -0.3
a1    = 0.5
sigma = 0.2

x = np.random.uniform(size=N)
y = a0 + a1 * x
t = y + np.random.standard_normal(size=y.shape) * sigma

fig = go.Figure()
trace_y = go.Scatter(x=x, y=y, mode="lines+markers", name="true reaction times")
fig.add_trace(trace_y)
trace_t = go.Scatter(x=x, y=t, mode="markers", name="noisy reaction times")
fig.add_trace(trace_t)
fig.update_xaxes(title_text="Grating Contrast")
fig.update_yaxes(title_text="Reaction Time")
fig.show()
