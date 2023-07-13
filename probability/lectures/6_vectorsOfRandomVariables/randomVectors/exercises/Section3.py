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


def Coloring(Covariance_y):
    
    rng = np.random.default_rng()
    
    Mean_x = np.array([0,0])
    Covariance_x = np.array([[1,0],[0,1]])
    
    X = rng.multivariate_normal(Mean_x, Covariance_x, size=2000)
    plt.figure()
    plt.plot(X[:, 0], X[:, 1], '.', alpha=0.5)
    plt.xlabel('x_1', fontsize=20)
    plt.ylabel('x_2', fontsize=20)
    
    eigenvalues, eigenvectors = np.linalg.eig(Covariance_y)
    
    EIG= np.power(eigenvalues,1/2)
    
    eigenvalues_EIG = np.diag(EIG)
    
    C =  eigenvectors @ eigenvalues_EIG


    Y = C@X.T
    
    print(np.shape(Y))
    
    plt.figure()
    plt.plot(Y[0, :], Y[1, :], '.', alpha=0.5)
    plt.xlabel('y_1', fontsize=20)
    plt.ylabel('y_2', fontsize=20)
    
##Coloring

K_y = np.array([[9,7],[7,8]])

Coloring(K_y)




