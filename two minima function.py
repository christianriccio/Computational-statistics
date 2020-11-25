#!/usr/bin/env python
# coding: utf-8

# In[3]:


from math import sqrt
from numpy import arange
from numpy.linalg import inv
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


# In[11]:


def backtracking(func, x, alpha_0, gradiente ): 
    r=(math.sqrt(5)+1)/2
    b=1/r
    alpha = alpha_0
    x_old = x
    hessiano=hessian_f(x)
    inv_hess = inv(hessian_f(x))
    x_new = x_old - alpha * np.dot(inv_hess,gradiente_f(x_old))
    while func(x_new)>func(x_old):
        alpha = b * alpha
        x_new = x_old - alpha * np.dot(inv_hess,gradiente_f(x_new))
    
    return alpha


def funzione(array):
    return ((array[1]-array[0])**4+8*array[0]*array[1]-array[0]+array[1]+3)
    
def dfdx(array):
    return -4*(array[1]-array[0])**3+8*array[1]-1

def dfdy(array):
    return 4*(array[1]-array[0])**3+8*array[0]+1


def gradiente_f(array):
    return np.array([dfdx(array), dfdy(array)])

def hessian_f(array):
    return np.array([[12*(array[1]-array[0])**2,8-12*(array[1]-array[0])**2],[8-12*(array[1]-array[0])**2,12*(array[1]-array[0])**2]])

def newton_rap(func, alpha_0, x_0,tol=10**-4, max_iter=1000):
    x=x_0
    it = 0
    gradiente = gradiente_f(x)
    hessiano=hessian_f(x)
    while max(np.abs(gradiente)) > tol and it < max_iter:
        gradiente = gradiente_f(x)
        inv_hess = inv(hessian_f(x))
        p = (-1)*np.dot(inv_hess, gradiente)
        x = x + backtracking(func, x, alpha_0, gradiente) * p
        it += 1
    return x


# In[5]:


x=np.linspace(-8,20, 1000)
y=np.linspace(-8,20, 1000)  


# In[25]:


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


# In[12]:


alpha_0=0.01
a=np.array([1,2])

out=newton_rap(funzione, alpha_0, a)
print(f'''punto di minimo: {out}
valore della funzione nel minimo {np.round(funzione(out),6)}
valore della derivata nel minimo {np.round(gradiente_f(out),6)}
il valore dell'hessiano è:\n{np.round(hessian_f(out),6)}''')


# In[13]:


a=np.array([-1,-2])
alpha_0=0.01
out=newton_rap(funzione, alpha_0, a)
print(f'''punto di minimo: {out}
valore della funzione nel minimo {np.round(funzione(out),6)}
valore della derivata nel minimo {np.round(gradiente_f(out),6)}
il valore dell'hessiano è:\n{np.round(hessian_f(out),6)}''')


# In[ ]:





# In[ ]:




