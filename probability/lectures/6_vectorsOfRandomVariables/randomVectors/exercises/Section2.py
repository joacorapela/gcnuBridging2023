# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:04:54 2023

@author: mohadeseh

"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.stats import multivariate_normal
from matplotlib import cm
import plotly.graph_objects as go
from matplotlib.ticker import LinearLocator


def Whitening(Mean_x,Covariance_x):
    
    rng = np.random.default_rng()
    
    X = rng.multivariate_normal(Mean_x, Covariance_x, size=2000)
    plt.figure()
    plt.plot(X[:, 0], X[:, 1], '.', alpha=0.5)
    plt.xlabel('x_1', fontsize=20)
    plt.ylabel('x_2', fontsize=20)
    
    eigenvalues, eigenvectors = np.linalg.eig(Covariance_x)
    
    EIG= np.power(eigenvalues,-1/2)
    
    eigenvalues_EIG = np.diag(EIG)
    
    W = eigenvalues_EIG @ eigenvectors.T


    Y = W@X.T
    
    print(np.shape(Y))
    
    plt.figure()
    plt.plot(Y[0, :], Y[1, :], '.', alpha=0.5)
    plt.xlabel('y_1', fontsize=20)
    plt.ylabel('y_2', fontsize=20)
    
##Whitening

Mu_x = np.array([0,0])
K_x = np.array([[5,-4],[-4,5]])

Whitening(Mu_x,K_x)




