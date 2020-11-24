#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import math

np.random.seed(seed=10)


# In[152]:


def funzione(x):
    y = x**2+2*np.exp(-x)
    return y

def funzione1(x):
    return (x-1.5)**2

def funzione2(x):
    return np.abs(x-3)+np.sin(x)-np.abs(x-2)

def plot(array, a):
    return plt.plot(array, a)

def bracketing(func, delta, p):
    R=(math.sqrt(5)+1)/2
    x=0
    x1=x*delta*p
    f1=func(x1)
    x2=x+delta*R*p
    f2=func(x2)
    j=1
    while f1>f2:
        j=j+1
        if delta > 20:
            print('star with a smaller value of delta')
        break
        x1=x2
        f1=f2
        x2=x+delta*(R**j)*p
        f2=func(x2)
   
    return x2

# use bracketing in combo with tri_sec and golden search

def tri_section(func, x,p, epsilon=10**-8, max_iter= 100):
    conta = 0
    x1=min(x)
    x2=max(x)
    delta=x2-x1
    while delta > epsilon and conta < max_iter:
        conta+=1
        x3=bracketing(func, delta, p)+delta/3
        x4=bracketing(func, delta, p)-delta/3
        f3 = func(x3)
        f4 = func(x4)    
        if f3>f4:
            x1=x3
        else:        
            x2=x4
        
        delta=x2-x1
        
    return np.round((x2+x1)/2, 6)
    
    
def golden_se(func, x, p):
    x1=min(x)
    x2=max(x)
    delta=x2-x1
    R=(math.sqrt(5)+1)/2
    epsilon=10**-6
    max_iter= 10000
    conta = 0
    while delta > epsilon and conta < max_iter:
        conta+=1
        x1=bracketing(func, delta, p)
        x2=bracketing(func, delta, p)
        x3=x2-delta/R
        x4=x1+delta/R
        f3 = func(x3)
        f4 = func(x4)    
        if f3>=f4:
            x1=x3
            x3=x4
            x4=x1+delta/R
            f4=func(x4)
        
        else: 
            x2=x4
            x4=x3
            x3=x2-delta/R
            f3=func(x3)
        
        
        delta=x2-x1


    return np.round((x2+x1)/2, 6), f'iterazione: {conta}' 


        


# In[114]:


x=np.linspace(0,2, 200)
plot(x, funzione(x))


# In[115]:


delta=0.1
p=1

print(f'\nIl minimo si trova nel punto: {np.round(bracketing(funzione,delta, p), 5)}\nNel minimo la funzione vale: {np.round(funzione(bracketing(funzione,delta, p)),5)}')


# In[116]:


plot(x, funzione1(x))


# In[117]:


delta=0.1
p=1
print(f'\nIl minimo si trova nel punto: {np.round(bracketing(funzione1,delta, p), 5)}\nNel minimo la funzione vale: {np.round(funzione(bracketing(funzione1,delta, p)),5)}')


# # Solo bracketing su funzione periodica

# In[147]:


x=np.linspace(-4,8)
plot(x, funzione2(x))


# In[148]:


delta=0.01
print(f'Per j={c}:\nIl minimo si trova nel punto: {np.round(bracketing(funzione2,delta, p=20), 5)}\nNel minimo la funzione vale: {np.round(funzione2(bracketing(funzione2,delta, p=20)),5)}')


# # golden search che implementa bracketing

# In[149]:


x=np.linspace(-4,8)
p=1
min_=golden_se(funzione, x,p)
print('minimo: ', min_)


# # tri-section che implementa bracketing

# In[151]:


x=np.linspace(-4,8)
p=0.1
print(tri_section(funzione2, x,p))


# In[ ]:




