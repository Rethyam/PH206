# -*- coding: utf-8 -*-
"""Lab_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hoc-5ka3wtUA6ubF_6vMSUQnT2Zd1Gub
"""

# LU Decomposition of Matrix A

import numpy as np   
import math as math  

A = np.array([[4, 3, 2, 1],[3, 3, 2, 1],[2, 2, 2, 1], [1, 1, 1, 1]],float)
n = A.shape[0]
b = np.array([1, 2, 3, 4], float)
U = A.copy()
L = np.eye(n, dtype=np.double)
    
for i in range(n):    
       
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
print(L)
print("\n")
print(U)

# LU Decomposition

import numpy as np   
import math as math  

A = np.array([[4, 3, 2, 1],
              [3, 3, 2, 1],
              [2, 2, 2, 1],
              [1, 1, 1, 1]],float)

b=np.array([20,18,14,8],float)

n = A.shape[0]
U = A.copy()
L = np.eye(n, dtype=np.double)
    
for i in range(n):    

        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]

result =np.array([[0.0] * len(A) for _ in range(len(A))],float)

 
for i in range(len(L)):
 
    for j in range(len(U[0])):
 
        for k in range(len(U)):
            result[i][j] += L[i][k] * U[k][j]

print(L)
print("\n")
print(U)
print("\n")
print(result)

def forward_subs(L,b):
    y= []
    for i in range(len(b)):
        y.append(b[i])
        for j in range(i):
            y[i]=y[i]-(L[i,j]*y[j])
        y[i]=y[i]/L[i,i]
    return y

def back_subs(U,y):
    x=np.zeros_like(y)
    for i in range(len(x),0,-1):
      x[i-1]=(y[i-1]-np.dot(U[i-1,i:],x[i:]))/U[i-1,i-1]
    return x

def solve_system_LU(L,U,b):
    y=forward_subs(L,b)
    x=back_subs(U,y)
    return x
print("\n")

ans=solve_system_LU(L,U,b)
print(ans)

# The Final Answer to the given Problem.

import numpy as np
import math as math 
np.set_printoptions(precision=3, suppress=True)

a=np.array([[4 , 3 , 2 , 1 ] ,
            [3 , 3 , 2 , 1 ] ,
            [2 , 2 , 2 , 1 ] ,
            [1 , 1 , 1 , 1 ]], float)

b=np.array([20,18,14,8],float)

l = np.array([[0.0] * len(a) for _ in range(len(a))],float)
l_transpose = np.array([[0.0] * len(a) for _ in range(len(a))],float)
n=len(a)


for k in range (n):
   
    for i in range (0,k):
        sum=0
        for j in range (i):
            sum=sum+ (l[i][j]*l[k][j])

        l[k][i]= (a[k][i]- sum)/l[i][i]


    sum1=0 
    for j in range (0,k):
        sum1=sum1 + (l[k][j]*l[k][j])

    l[k][k]= math.sqrt(a[k][k]-sum1)

for i in range (n):
    for j in range (i+1):
        l_transpose[j][i]=l[i][j]



result =np.array([[0.0] * len(a) for _ in range(len(a))],float)
 
for i in range(len(l)):
 
    for j in range(len(l_transpose[0])):
 
        for k in range(len(l_transpose)):
            result[i][j] += l[i][k] * l_transpose[k][j]
 
print (l)
print("\n")
print (l_transpose)
print("\n")
print(result)

def forward_subs(L,b):
    y= []
    for i in range(len(b)):
        y.append(b[i])
        for j in range(i):
            y[i]=y[i]-(L[i,j]*y[j])
        y[i]=y[i]/L[i,i]

    return y

def back_subs(U,y):
    x=np.zeros_like(y)
    for i in range(len(x),0,-1):
      x[i-1]=(y[i-1]-np.dot(U[i-1,i:],x[i:]))/U[i-1,i-1]

    return x

def solve_system_LU(L,U,b):
    y=forward_subs(L,b)
    x=back_subs(U,y)

    return x
print("\n")

ans=solve_system_LU(l,l_transpose,b)
print(ans)