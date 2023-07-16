

"""
Predictive distribution
=======================

The code below demonstrates the use of the predictive distribution in Bayesian
linear regression.

"""

#%%
# Import requirments
# ------------------

import numpy as np
import scipy.stats
import plotly.graph_objects as go

import joacorapela_common.stats.bayesianLinearRegression

#%%
# Define a function to generate sinusoidal regression data
# --------------------------------------------------------

def generateData(x, true_coefs, sigma=0.1):
    y = true_coefs[0] + true_coefs[1] * x
    t = y + np.random.normal(loc=0, scale=sigma, size=len(y))
    return y, t


#%%
# Define functions to generate the design matrix sinusoidal regression data
# -------------------------------------------------------------------------

def getLinearBasisFunctions():
    M = 2
    basis_functions = [None for m in range(M)]
    basis_functions[0] = lambda x: 1.0 if isinstance(x, float) else np.ones(len(x))
    basis_functions[1] = lambda x: x
    return basis_functions


def buildDesignMatrixRow(x, basis_functions):
    M = len(basis_functions)
    design_matrix_row = np.empty(shape=M, dtype=np.double)
    for m in range(M):
        design_matrix_row[m] = basis_functions[m](x)
    return design_matrix_row


def buildDesignMatrix(x, basis_functions):
    M = len(basis_functions)
    N = len(x)
    design_matrix = np.empty(shape=(N, M), dtype=np.double)
    for n in range(N):
        design_matrix[n,:] = buildDesignMatrixRow(x=x[n],
                                                          basis_functions=basis_functions)
    return design_matrix


#%%
# Generate train data
# -------------------

# N = 4
# N = 10
N = 25
true_coefs = [1.0, 2.0]
x = np.sort(np.random.uniform(size=N))
_, t = generateData(x=x, true_coefs=true_coefs)
x_dense = np.linspace(0, 1, 1000)
y_dense, _ = generateData(x=x_dense, true_coefs=true_coefs)

#%%
# Plot train data
# ---------------

fig = go.Figure()
trace_true = go.Scatter(x=x_dense, y=y_dense, mode="lines", line_color="green")
trace_data = go.Scatter(x=x, y=t, mode="markers", marker_color="blue")
fig.add_trace(trace_true)
fig.add_trace(trace_data)
fig.update_layout(xaxis_title="independent variable",
                  yaxis_title="dependent variable",
                  showlegend=False)
fig

#%%
# Get and plot the basis functions
# --------------------------------

basis_functions = getLinearBasisFunctions()

fig = go.Figure()
for i in range(len(basis_functions)):
    basis_function_values = basis_functions[i](x_dense)
    trace = go.Scatter(x=x_dense, y=basis_function_values, mode="lines")
    fig.add_trace(trace)
fig.update_layout(xaxis_title="x",
                  yaxis_title=r"$\phi_i(x)$",
                  showlegend=False)
fig

#%%
# Build design matrix
# -------------------

Phi = buildDesignMatrix(x=x, basis_functions=basis_functions)

#%%
# Estimate least-square parameters
# -------------------------------

w_hat = np.linalg.solve(np.dot(Phi.T, Phi), np.dot(Phi.T, t))

#%%
# Predict training data
# ---------------------

y_hat = np.dot(Phi, w_hat)

#%%
# Plot predictions
# ----------------

fig = go.Figure()
trace_true = go.Scatter(x=x_dense, y=y_dense, mode="lines", line_color="green")
trace_data = go.Scatter(x=x, y=t, mode="markers", marker_color="blue",
                        marker_symbol="circle-open", marker_size=10)
trace_predictions = go.Scatter(x=x, y=y_hat, mode="markers", marker_color="red",
                        marker_symbol="cross", marker_size=10)
fig.add_trace(trace_true)
fig.add_trace(trace_data)
fig.add_trace(trace_predictions)
fig.update_layout(xaxis_title="independent variable",
                  yaxis_title="dependent variable",
                  title=(f"true-estimated_intercept={true_coefs[0]-w_hat[0]:.4f}, "
                         f"true-estimated_slope={true_coefs[1]-w_hat[1]:.4f}"),
                  showlegend=False)
fig

breakpoint()
