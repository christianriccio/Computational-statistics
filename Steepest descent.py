#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
from math import exp
import matplotlib.pyplot as plt
from random import choice
from numpy import arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show,figure
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt



np.random.seed(seed=10)


# In[4]:


# 1 - variable 
def funzione(x):
    return np.exp(-x)+x**4


def plot(array, func):
    return plt.plot(array, func)


def steepest_descent(step_size, alpha, tollerance, itera, x, gradiente):
    i=0
    while step_size > tol and i < max_iter:
        x_old = x 
        x = x - alpha * gradiente(x_old) 
        step_size = abs(x - x_old) #differenza tra le iterazioni consecutive
        i = i+1
        
    return i, x, funzione(x)


# 2 - variables
def funzione2_d(array):
    return array[0]*2+array[0]*array[1]+3*array[1]**2
    
def dfdx(array):
    return 2*array[0]-array[1]

def dfdy(array):
    return -array[0]+6*array[1]

def gradiente_f(array):
    return np.array([dfdx(array), dfdy(array)])

def grad_descent(f, gradiente_f, alpha, tol=10**-6, max_iter=1000):
    x=np.array([1,2])
    it = 0
    while max(np.abs(gradiente_f(x)))> tol and it < max_iter:
        x=x-alpha*gradiente_f(x)
        it += 1
    print('iterazione', it)
    return x


# In[5]:


x=np.linspace(-8,20, 1000)
plot(x, funzione(x))


# In[6]:


x = np.random.random()
print(f'starting point: {x}')
alpha = 0.1
tol = 10**-6 
step = 1 
max_iter = 1000
grad= lambda x: 4*x**3-exp(-x)
a,b,c=steepest_descent(step, alpha, tol, max_iter, x, grad)

print(f'Alla iterazione {a}:\n il minimo della funzione vale:{np.round(b,7)}\n in tale punto la funzione vale {np.round(funzione(c),7), }')


# In[ ]:





# In[7]:


x=np.linspace(-8,20, 1000)
y=np.linspace(-8,20, 1000)

X,Y = meshgrid(x, y) # grid of point
f = funzione2_d([X,Y])

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, f, rstride=1, cstride=1, 
                      cmap=cm.RdBu,linewidth=0, antialiased=False)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


# In[9]:


alpha=0.1
out=grad_descent(funzione, gradiente_f, alpha)
print(f'il punto di minimo trovato è: {np.round(out,10)}\n la funzione  nel punto vale: {np.round(funzione(out),10)}\n il gradiente di f nel punto vale: {np.round(gradiente_f(out),10)}')


# In[ ]:




