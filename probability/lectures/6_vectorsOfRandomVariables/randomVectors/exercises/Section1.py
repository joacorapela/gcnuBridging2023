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

#%% A function to plot the PDF and CDF surfaces for a 2D Gaussian
def Plot_pdf_CDF_2D(Mean,Covariance):
    #plot pdf surface
    x, y = np.mgrid[Mean[0]-3*Covariance[0,0]:Mean[0]+3*Covariance[0,0]:.1, Mean[1]-3*Covariance[1,1]:Mean[1]+3*Covariance[1,1]:.1]
    pos = np.dstack((x, y))
    rv = multivariate_normal(Mean,Covariance)
    
    pdf = rv.pdf(pos)
    CDF = rv.cdf(pos)
    #plot PDF
    fig, ax = plt.subplots(1,2,subplot_kw={"projection": "3d"})

    surf = ax[0].plot_surface(x, y, pdf, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    ax0 =ax[0]
    fontsize = 20
    ax0.zaxis.set_major_locator(LinearLocator(10))
    ax0.zaxis.set_major_formatter('{x:.02f}')
    #fig.colorbar(surf, shrink=0.5, aspect=5)
    ax0.set_xlabel('x',fontname="Arial", fontsize= fontsize)
    ax0.set_ylabel('y',fontname="Arial", fontsize= fontsize)
    ax0.set_zlabel('pdf',fontname="Arial", fontsize= fontsize)
    
    #plot CDF
    surf = ax[1].plot_surface(x, y, CDF, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    ax1 =ax[1]
    fontsize = 20
    ax1.zaxis.set_major_locator(LinearLocator(10))
    ax1.zaxis.set_major_formatter('{x:.02f}')
    #fig.colorbar(surf, shrink=0.5, aspect=5)
    ax1.set_xlabel('x',fontname="Arial", fontsize= fontsize)
    ax1.set_ylabel('y',fontname="Arial", fontsize= fontsize)
    ax1.set_zlabel('CDF',fontname="Arial", fontsize= fontsize)
    plt.show()

#%%A function to plot the PDF and CDF surfaces for a 3D Gaussian
def Plot_pdf_CDF_3D(Mean,Covariance):
    number_of_points = 20
    Dimention = number_of_points**3
    x_1 = np.linspace(Mean[0]-2*Covariance[0,0],Mean[0]+2*Covariance[0,0],number_of_points)
    x_2 = np.linspace(Mean[1]-2*Covariance[1,1],Mean[1]+2*Covariance[1,1],number_of_points)
    x_3 = np.linspace(Mean[2]-2*Covariance[2,2],Mean[2]+2*Covariance[2,2],number_of_points)

    x_1,x_2,x_3 = np.meshgrid(x_1, x_2, x_3)

    x_1 =np.array(x_1).reshape(Dimention,)
    x_2 = np.array(x_2).reshape(Dimention,)
    x_3 =np.array(x_3).reshape(Dimention,)

    pos = np.dstack((x_1, x_2, x_3))
    pos = np.array(pos).reshape(Dimention,3)

    rv = multivariate_normal(Mean, Covariance)

    #pdf for £D guassian
    c =  multivariate_normal.pdf(pos, mean = Mean, cov=Covariance)
    c = np.array(c).reshape(Dimention,)

    fig, ax = plt.subplots(1,2,subplot_kw={"projection": "3d"})
    img = ax[0].scatter(x_1, x_2, x_3, c=c, cmap='YlOrRd', alpha=1)

    ax0 =ax[0]
    fontsize = 30
    ax0.zaxis.set_major_locator(LinearLocator(10))
    ax0.zaxis.set_major_formatter('{x:.02f}')
    #fig.colorbar(surf, shrink=0.5, aspect=5)
    ax0.set_xlabel('x',fontname="Arial", fontsize= fontsize)
    ax0.set_ylabel('y',fontname="Arial", fontsize= fontsize)
    ax0.set_zlabel('z',fontname="Arial", fontsize= fontsize)
    ax0.set_title('pdf',fontname="Arial", fontsize= fontsize)

    #CDF for 3D guassian
    c =  multivariate_normal.cdf(pos, mean = Mean, cov=Covariance)
    c = np.array(c).reshape(Dimention,)
    img = ax[1].scatter(x_1, x_2, x_3, c=c, cmap='YlOrRd', alpha=1)

    ax0 =ax[1]
 
    ax0.zaxis.set_major_locator(LinearLocator(10))
    ax0.zaxis.set_major_formatter('{x:.02f}')
    #fig.colorbar(surf, shrink=0.5, aspect=5)
    ax0.set_xlabel('x',fontname="Arial", fontsize= fontsize)
    ax0.set_ylabel('y',fontname="Arial", fontsize= fontsize)
    ax0.set_zlabel('z',fontname="Arial", fontsize= fontsize)
    ax0.set_title('CDF',fontname="Arial", fontsize= fontsize)

    plt.show()

#%% Step 1:2D
#For this interesting distribution, implement step 1 to see what pdf and CDF look like, for different mean vector and covariance matrices!    
Mean = np.array([0,0])
Covariance = np.array([[9,-8],[-8,9]])
Plot_pdf_CDF_2D(Mean,Covariance)
#CDF-PDF example

#%% Step 2: 3D
Mean = np.array([0,0,0])
Covariance = np.array([[3, 2, 2], [2, 3,2], [2, 2,3]])
Plot_pdf_CDF_3D(Mean,Covariance)


