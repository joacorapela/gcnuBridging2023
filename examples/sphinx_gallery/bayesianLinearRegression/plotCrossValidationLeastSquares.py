

"""
Cross-validation for least-squares regression
=============================================

Calculate the root-mean-square error of a polynomial regression for train and
test data.

"""

#%%
# Import requirments
# ------------------

import numpy as np
import plotly.graph_objects as go

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
# Generate train and test data
# ----------------------------

# N = 4
# N = 10
# N = 15
N = 100
x = np.sort(np.random.uniform(size=N))
_, t_train = generateData(x=x)
_, t_test = generateData(x=x)

Ms = np.arange(10)
train_NRMSEs = [None for m in Ms]
test_NRMSEs = [None for m in Ms]
for M in Ms:
    basis_functions = getPolynomialBasisFunctions(M=M)
    Phi = buildDesignMatrix(x=x, basis_functions=basis_functions)
    w_hat = np.linalg.solve(np.dot(Phi.T, Phi),
                            np.dot(Phi.T, t_train))
    predictions = np.dot(Phi, w_hat)
    train_NRMSEs[M] = np.mean((predictions-t_train)**2)
    test_NRMSEs[M] = np.mean((predictions-t_test)**2)

#%%
# Plot NRMSEs
# ----------

fig = go.Figure()
trace_train = go.Scatter(x=Ms, y=train_NRMSEs, mode="lines+markers",
                         line=dict(color="blue"), name="Train")
trace_test = go.Scatter(x=Ms, y=test_NRMSEs, mode="lines+markers",
                        line=dict(color="red"), name="Test")
fig.add_trace(trace_train)
fig.add_trace(trace_test)
fig.update_layout(xaxis_title="M", yaxis_title="Root-Mean-Square Error")
fig.update_yaxes(range=[0.0, 1.0])
fig
