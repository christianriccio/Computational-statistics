#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[11]:


def funzione(x):
    y = x**2+2*np.exp(-x)
    return y

def plot(array, a):
    return plt.plot(array, a)

def golden_se(funzione, x):
    x1=min(x)
    x2=max(x)
    delta=x2-x1
    R=(math.sqrt(5)+1)/2
    epsilon=10**-6
    max_iter= 1000
    conta = 0
    while delta > epsilon and conta < max_iter:
        conta+=1
        x3=x2-delta/R
        x4=x1+delta/R
        f3 = funzione(x3)
        f4 = funzione(x4)    
        if f3>=f4:
            x1=x3
            x3=x4
            x4=x1+delta/R
            f4=funzione(x4)
        
        else: 
            x2=x4
            x4=x3
            x3=x2-delta/R
            f3=funzione(x3)
        
        
        delta=x2-x1


    return np.round((x2+x1)/2, 6), f'iterazione: {conta}' 


# In[6]:


x=np.linspace(0,2, 200)
plot(x, funzione(x))


# In[12]:


print(f"minimum of the function': {golden_se(funzione, x)}")


# In[ ]:




