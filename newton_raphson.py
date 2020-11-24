#!/usr/bin/env python
# coding: utf-8

# In[5]:


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


# In[6]:


# 1 -  variable

def funzione(x):
    return np.exp(-x)+x**4

def gradiente_f(x):
    return 4*x**3-np.exp(-x)

def hessian_f(x):
    return 12*x**2+np.exp(-x)

def backtracking(func, x, alpha_0, gradiente ): 
    r=(math.sqrt(5)+1)/2
    b=1/r
    alpha = alpha_0
    x_old = x
    x_new = x_old - alpha * gradiente
    while func(x_new)>func(x_old):
        alpha = b * alpha
        x_new = x_old - alpha * gradiente  
    
    return alpha

def plot(array, func):
    return plt.plot(array, func)


def newton_rap(func, alpha_0, x_0, tol=10**-6, max_iter=1000):
    x=x_0
    it = 0

    gradiente=gradiente_f(x)
    hessiano=hessian_f(x)
    while np.max(np.abs(gradiente)) > tol:
        it += 1
        p = - gradiente/hessiano
        x = x + backtracking(func, x, alpha_0, gradiente) * p
        f=func(x)
        gradiente=gradiente_f(x)
    print('tot iterazioni', it)
    return x



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



# In[7]:


x=np.linspace(-8,20, 1000)
plot(x, funzione(x))


# In[8]:


alpha=0.01
a=-1
out=newton_rap(funzione, alpha, a)
print(f'minimo della funzione:{np.round(out,6)}\nvalore della funzione nel minimo {np.round(funzione(out),6)}\nvalore della derivata nel minimo {np.round(gradiente_f(out),5)}\nvalore della derivata seconda nel minimo {np.round(hessian_f(out),6)}')


# In[ ]:


# 2 variables newton-raphson


# In[9]:


def funzione(array):
    return array[0]**2+array[0]*array[1]+3*array[1]**2
    
def dfdx(array):
    return 2*array[0]-array[1]

def dfdy(array):
    return -array[0]+6*array[1]


def gradiente_f(array):
    return np.array([dfdx(array), dfdy(array)])

def hessian_f(array):
    return np.array([[2,-1],[-1,6]])

def newton_rap(func, alpha_0, x_0, tol=10**-6, max_iter=1000):
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
    print('tot iterazioni', it)
    return x


# In[10]:


x=np.linspace(-8,20, 1000)
y=np.linspace(-8,20, 1000)  


# In[11]:


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


alpha_0=0.1
a=np.array([1,2])

out=newton_rap(funzione, alpha_0, a)
print(f'''punto di minomo: {out}
valore della funzione nel minimo {funzione(out)}
valore della derivata nel minimo {gradiente_f(out)}
il valore dell'hessiano è:\n{hessian_f(out)}''')


# In[13]:


# Use of the Hessian into the backtracking 


# In[14]:


def backtracking_hess(func, x, alpha_0, gradiente ): 
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

def newton_rap(func, alpha_0, x_0, tol=10**-6, max_iter=1000):
    x=x_0
    it = 0
    gradiente = gradiente_f(x)
    hessiano=hessian_f(x)
    while max(np.abs(gradiente)) > tol and it < max_iter:
        gradiente = gradiente_f(x)
        inv_hess = inv(hessian_f(x))
        p = (-1)*np.dot(inv_hess, gradiente)
        x = x + backtracking_hess(func, x, alpha_0, gradiente) * p
        it += 1
    print('tot iterazioni', it)
    return x


# In[15]:


alpha_0=0.1
a=np.array([1,2])

out=newton_rap(funzione, alpha_0, a)
print(f'''punto di minomo: {out}
valore della funzione nel minimo {funzione(out)}
valore della derivata nel minimo {gradiente_f(out)}
il valore dell'hessiano è:\n{hessian_f(out)}''')


# In[ ]:




