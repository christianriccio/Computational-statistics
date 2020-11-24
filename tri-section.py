#!/usr/bin/env python
# coding: utf-8

# # tri- section optimization method
# 
# 
# 

# In[10]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[11]:


def funzione(x):
    y = x**2+2*np.exp(-x)
    return y

def funzione1(x):
    return (x-1.5)**2

def plot(array, a):
    return plt.plot(array, a)

def tri_section(func, x, epsilon=10**-6, max_iter= 100):
    x1=min(x)
    x2=max(x)
    delta=x2-x1
    conta = 0
    while delta > epsilon and conta < max_iter:
        conta+=1
        x3=x1+delta/3
        x4=x2-delta/3
        f3 = funzione(x3)
        f4 = funzione(x4)    
        if f3>f4:
            x1=x3
        else:        
            x2=x4
        
        delta=x2-x1
        
    return np.round((x2+x1)/2, 6)

    


# In[12]:


x=np.linspace(0,2, 200)
plot(x, funzione(x))

plot(x, funzione1(x))



print(f'the minimum of the functio is: {tri_section(funzione, x)}')

print(f'minimum of the functio is: {tri_section(funzione1, x)}')



