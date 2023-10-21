

"""
Plot model evidence
===================

Plot the evidence of models of different polynomial order.

"""

#%%
# Import requirments
# ------------------

import numpy as np
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
# Define function to compute the log model evidence
# -------------------------------------------------

def computeLogEvidence(N, M, mN, SN, Phi, t,
                       prior_precision, likelihood_precision):
    EmN = (likelihood_precision/2.0*np.linalg.norm(t-np.dot(Phi, mN), 2)**2 +
           prior_precision/2.0*np.linalg.norm(mN, 2)**2)
    log_model_evidence = (M/2.0 * np.log(prior_precision) +
                          N/2.0 * np.log(likelihood_precision) -
                          EmN +
                          0.5 * np.log(np.linalg.det(SN)) -
                          N/2.0 * np.log(2*np.pi))
    return log_model_evidence

#%%
# Generate train and test data
# ----------------------------

# N = 4
N = 10
# N = 15
# N = 100
x = np.sort(np.random.uniform(size=N))
_, t = generateData(x=x)

#%%
# Set estimation parameters
# -------------------------

prior_precision = 0.005
likelihood_precision = 9.0

#%%
# Calculate model evindences
# --------------------------

Ms = np.arange(10)
log_evidences = [None for m in Ms]
for M in Ms:
    basis_functions = getPolynomialBasisFunctions(M=M)
    Phi = buildDesignMatrix(x=x, basis_functions=basis_functions)
    mN, SN = \
        joacorapela_common.stats.bayesianLinearRegression.batchWithSimplePrior(
            Phi=Phi, y=t, alpha=prior_precision, beta=likelihood_precision)
    log_evidences[M] = computeLogEvidence(
        N=N, M=M, mN=mN, SN=SN, Phi=Phi, t=t,
        prior_precision=prior_precision,
        likelihood_precision=likelihood_precision)

#%%
# Plot models' log evidences
# --------------------------

fig = go.Figure()
trace = go.Scatter(x=Ms, y=log_evidences, mode="lines+markers",
                   line=dict(color="blue"))
fig.add_trace(trace)
fig.update_layout(xaxis_title="M",
                  yaxis_title=r"$\log p(\mathbf{t}|\alpha,\beta)$")
fig

