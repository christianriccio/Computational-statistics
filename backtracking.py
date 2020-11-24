#!/usr/bin/env python
# coding: utf-8

# In[97]:


from math import sqrt
from numpy import arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show,figure
import numpy as np
import math
from math import exp
import matplotlib.pyplot as plt
from random import choice
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt


np.random.seed(seed=10)


# In[149]:


def backtracking(func, x, alpha_0, gradiente ): 
    r=(math.sqrt(5)+1)/2
    b=1/r
    alpha = alpha_0
    x_old = x
    x_new = x_old - alpha * gradiente_f(x_old)
    while func(x_new)>func(x_old):
        alpha = b * alpha
        x_new = x_old - alpha * gradiente_f(x_new)  
    
    return alpha


def funzione(array):
    return array[0]**2-array[0]*array[1]+3*array[1]**2
    
def dfdx(array):
    return 2*array[0]-array[1]

def dfdy(array):
    return -array[0]+6*array[1]

def gradiente_f(array):
    return np.array([dfdx(array), dfdy(array)])

def grad_descent_back(func, alpha_0, x_0, tol=10**-6, max_iter=1000):
    x=x_0
    it = 0
    gradiente = gradiente_f(x)
    while max(np.abs(gradiente)) > tol and it < max_iter:
        gradiente = gradiente_f(x)
        p = (-1)*gradiente
        x = x + backtracking(func, x, alpha_0, gradiente) * p
        it += 1
    print('tot iterazioni', it)
    return x


# In[150]:


x=np.linspace(-8,20, 1000)
y=np.linspace(-8,20, 1000)    


# In[151]:


X,Y = meshgrid(x, y) # grid of point
f = funzione([X, Y])

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, f, rstride=1, cstride=1, 
                      cmap=cm.RdBu,linewidth=0, antialiased=False)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


# In[153]:


alpha_0=0.1
a=np.array([1,2])

out=grad_descent_back(funzione, alpha_0, a)
print(f'punto di minomo: {out}\nvalore della funzione nel minimo {funzione(out)}\nvalore della derivata nel minimo {gradiente_f(out)}')


# In[ ]:




