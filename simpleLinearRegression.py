# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 18:55:05 2016
"""

import numpy as np
import matplotlib.pyplot as plt

def hypothesisFunction(x, theta0, theta1):
    h = []
    for i in range(len(x)) :
        h.append(theta0 + theta1*x[i])
    return h
    
def costFunction(x,y,theta0,theta1) :
    h = hypothesisFunction(x,theta0, theta1)
    tmp = np.subtract(h,y)
    J = 1/float(2*len(x)) * np.sum(np.power(tmp,2))
    return J
    
def gradientDescent(x,y,theta0,theta1,alpha,tol):
    iter = 1
    J_old = 0
    J = costFunction(x,y,theta0,theta1)
    while np.absolute(J - J_old) > tol or iter < 2:
        J_old = J
        theta0_old = theta0
        theta1_old = theta1
        theta0 = updateTheta0(x,y,theta0_old,theta1_old,alpha)
        theta1 = updateTheta1(x,y,theta0_old,theta1_old,alpha)
        J = costFunction(x,y,theta0, theta1)
        iter = iter + 1
    print 'Number of iterations: ' + str(iter)
    return [theta0, theta1]
        
def updateTheta0(x,y,theta0,theta1,alpha) :
    m = len(x)
    h = hypothesisFunction(x, theta0, theta1)
    return theta0 - alpha * (1/float(m) * np.sum(np.subtract(h,y)))
    
def updateTheta1(x,y,theta0,theta1,alpha) :
    m = len(x)
    h = hypothesisFunction(x, theta0, theta1)
    tmp = np.subtract(h,y)
    return theta1 - alpha * (1/float(m) * np.sum(np.multiply(tmp,x)))

def main() :
    x = [0, 1, 2, 4]
    y = [1, 2, 3, 5]
    theta0 = 0
    theta1 = 0
    tol = 0.001
    alpha = 0.1 # Learning rate
    Theta = gradientDescent(x,y,theta0,theta1,alpha,tol)
    print 'Theta0, Theta1 = ' + str(Theta)
    
    h = hypothesisFunction(x, Theta[0], Theta[1])
    fig, ax = plt.subplots()
    ax.plot(x,y,'rx')
    ax.plot(x,h,'-')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show() 
    
main()
