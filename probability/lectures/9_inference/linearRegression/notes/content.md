# Overview

- probabilities

    - the multivariate Gaussian distribution

        - marginals are Gaussians

        - conditionals are Gaussians

- statistics

    - linear regression

        - deterministic regression

            - least squres 

            - regularized least squares

        - probabilistic regression

            - maximum likelihood

            - Bayesian

                - batch Bayesian linear regression

                - online Bayesian linear regression

                - predictive distribution

                - evaluation of the evidence function
                
        - inference in the linear Gaussian model

# 2.3 The Gaussian distribution

- 1D Gaussian -> MD Gaussian

- motivation

    - maximum entroy distribution for given mean and covariance

    - CLT (Simon Laplace inventor in 1810,  Adolphe Quetelet used it to show
    that soldier's chest girths follow a Gaussian distribution)

    - biography of Gauss

- mathematical description of ellipses

- eigenvalue transformation makes Gaussian random variables independent
    - uncorrelated Gaussian random variables are independent

- ellipsoid representation of Gaussian

- in the eigenvectors basis, correlated Gaussian random variables become
uncorrelated (i.e., independent)

- limitations of the Gaussian

    - overparametrized

        - overcoming overparametrizations (diagonal covariance, scaled identity)

    - unimodal

        - discrete latent variables: mixture of Gaussians

        - continuous latent variables: 

            - markov Random fields (images),

            - linear dynamical system (time series)

    - graphical models: language for describing joint distributions


## 2.3.1 Conditional Gaussian distributions

## 2.3.2 Marginal Gaussian distributions

## 2.3.3 Bayes' theorem for Gaussian variables

# 3 Linear models for regression

## 3.1 Linear basis function model

## Deterministic projections, least squares, normal equations

    - projections (lecture 6, Trefethen)

    - least squares (lecture 11, Trefethen)

    - 3.1.2 Geometry of least squares

    - 3.1.4 Regularized least squares

## 3.3 Bayesian linear regression

### 3.3.1 Parameter distribution

### 3.3.2 Predictive distribution

## 3.5 The evidence approximation
