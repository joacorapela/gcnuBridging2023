

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

def generateData(x, sigma=0.1):
    y = np.sin(2*np.pi*x)
    t = y + np.random.normal(loc=0, scale=sigma, size=len(y))
    return y, t


#%%
# Define functions to generate the design matrix sinusoidal regression data
# -------------------------------------------------------------------------

def getPolynomialBasisFunctions(M):
    basis_functions = [None for m in range(M+1)]
    for m in range(M+1):
        basis_functions[m] = lambda x, m=m: x**m
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
        design_matrix[n, :] = buildDesignMatrixRow(
            x=x[n], basis_functions=basis_functions)
    return design_matrix


#%%
# Define plotting functions
# -------------------------

def getPlotBasisFunctions(x_dense, basis_functions):
    fig = go.Figure()
    for i in range(len(basis_functions)):
        basis_function_values = basis_functions[i](x_dense)
        trace = go.Scatter(x=x_dense, y=basis_function_values, mode="lines",
                           name=r"$\phi_{:d}$".format(i))
        fig.add_trace(trace)
    fig.update_layout(xaxis_title="x", yaxis_title=r"$\phi_i(x)$",
                      showlegend=False)
    return fig


def getPlotPredictions(x_dense, true_dense, x, t, predictions_dense):
    fig = go.Figure()
    trace_true = go.Scatter(x=x_dense, y=true_dense, mode="lines",
                            line_color="green")
    trace_data = go.Scatter(x=x, y=t, mode="markers", marker_color="blue",
                            marker_symbol="circle-open", marker_size=10)
    trace_predictions = go.Scatter(x=x_dense, y=predictions_dense,
                                   mode="lines", line_color="red")
    fig.add_trace(trace_true)
    fig.add_trace(trace_data)
    fig.add_trace(trace_predictions)
    fig.update_layout(xaxis_title="independent variable",
                      yaxis_title="dependent variable",
                      title=f"M={M}", showlegend=False)
    fig.update_yaxes(range=[-1.5, 1.5])
    return fig

#%%
# Generate train data
# -------------------

# N = 4
# N = 10
# N = 15
N = 100
x = np.sort(np.random.uniform(size=N))
_, t = generateData(x=x)
x_dense = np.linspace(0, 1, 1000)
true_dense, _ = generateData(x=x_dense, sigma=0.0)

#%%
# Plot train data
# ---------------

fig = go.Figure()
trace_true = go.Scatter(x=x_dense, y=true_dense, mode="lines", line_color="green")
trace_data = go.Scatter(x=x, y=t, mode="markers", marker_color="blue")
fig.add_trace(trace_true)
fig.add_trace(trace_data)
fig.update_layout(xaxis_title="independent variable",
                  yaxis_title="dependent variable",
                  showlegend=False)
fig

#%%
# Set estimation parameters
# -------------------------

M = 0 # number of basis functions (excluding offset)

#%%
# Get and plot the basis functions
# --------------------------------

basis_functions = getPolynomialBasisFunctions(M=M)
fig = getPlotBasisFunctions(x_dense=x_dense, basis_functions=basis_functions)
fig

#%%
# Build design matrix
# -------------------

Phi = buildDesignMatrix(x=x, basis_functions=basis_functions)
Phi_dense = buildDesignMatrix(x=x_dense, basis_functions=basis_functions)

#%%
# Estimate least-square parameters
# -------------------------------

w_hat = np.linalg.solve(np.dot(Phi.T, Phi), np.dot(Phi.T, t))

#%%
# Predict training data
# ---------------------

predictions_dense = np.dot(Phi_dense, w_hat)

#%%
# Plot predictions
# ----------------

fig = getPlotPredictions(x_dense=x_dense, true_dense=true_dense, x=x, t=t,
                         predictions_dense=predictions_dense)
fig

#%%
# Set estimation parameters
# -------------------------

M = 1 # number of basis functions (excluding offset)

#%%
# Get and plot the basis functions
# --------------------------------

basis_functions = getPolynomialBasisFunctions(M=M)
fig = getPlotBasisFunctions(x_dense=x_dense, basis_functions=basis_functions)
fig

#%%
# Build design matrix
# -------------------

Phi = buildDesignMatrix(x=x, basis_functions=basis_functions)
Phi_dense = buildDesignMatrix(x=x_dense, basis_functions=basis_functions)

#%%
# Estimate least-square parameters
# -------------------------------

w_hat = np.linalg.solve(np.dot(Phi.T, Phi), np.dot(Phi.T, t))

#%%
# Predict training data
# ---------------------

predictions_dense = np.dot(Phi_dense, w_hat)

#%%
# Plot predictions
# ----------------

fig = getPlotPredictions(x_dense=x_dense, true_dense=true_dense, x=x, t=t,
                         predictions_dense=predictions_dense)
fig

#%%
# Set estimation parameters
# -------------------------

M = 3 # number of basis functions (excluding offset)

#%%
# Get and plot the basis functions
# --------------------------------

basis_functions = getPolynomialBasisFunctions(M=M)
fig = getPlotBasisFunctions(x_dense=x_dense, basis_functions=basis_functions)
fig

#%%
# Build design matrix
# -------------------

Phi = buildDesignMatrix(x=x, basis_functions=basis_functions)
Phi_dense = buildDesignMatrix(x=x_dense, basis_functions=basis_functions)

#%%
# Estimate least-square parameters
# -------------------------------

w_hat = np.linalg.solve(np.dot(Phi.T, Phi), np.dot(Phi.T, t))

#%%
# Predict training data
# ---------------------

predictions_dense = np.dot(Phi_dense, w_hat)

#%%
# Plot predictions
# ----------------

fig = getPlotPredictions(x_dense=x_dense, true_dense=true_dense, x=x, t=t,
                         predictions_dense=predictions_dense)
fig

#%%
# Set estimation parameters
# -------------------------

M = 9 # number of basis functions (excluding offset)

#%%
# Get and plot the basis functions
# --------------------------------

basis_functions = getPolynomialBasisFunctions(M=M)
fig = getPlotBasisFunctions(x_dense=x_dense, basis_functions=basis_functions)
fig

#%%
# Build design matrix
# -------------------

Phi = buildDesignMatrix(x=x, basis_functions=basis_functions)
Phi_dense = buildDesignMatrix(x=x_dense, basis_functions=basis_functions)

#%%
# Estimate least-square parameters
# -------------------------------

w_hat = np.linalg.solve(np.dot(Phi.T, Phi), np.dot(Phi.T, t))

#%%
# Predict training data
# ---------------------

predictions_dense = np.dot(Phi_dense, w_hat)

#%%
# Plot predictions
# ----------------

fig = getPlotPredictions(x_dense=x_dense, true_dense=true_dense, x=x, t=t,
                         predictions_dense=predictions_dense)
fig

