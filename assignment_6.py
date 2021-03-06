# -*- coding: utf-8 -*-
"""Assignment-6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c_oWMAet_GGqawxJbsp7JhlJDuNLMWNn
"""

from numpy import array,identity,diagonal
from math import sqrt
import numpy as np
def jacobi(a,tol = 1.0e-9): 
    def maxElem(a): 
        n = len(a)
        aMax = 0.0
        for i in range(n-1):
            for j in range(i+1,n):
                if abs(a[i,j]) >= aMax:
                    aMax = abs(a[i,j])
                    k = i; l = j
        return aMax,k,l
    def rotate(a,p,k,l): 
        n = len(a)
        aDiff = a[l,l] - a[k,k]
        if abs(a[k,l]) < abs(aDiff)*1.0e-36: t = a[k,l]/aDiff
        else:
            phi = aDiff/(2.0*a[k,l])
            t = 1.0/(abs(phi) + sqrt(phi**2 + 1.0))
            if phi < 0.0: t = -t
        c = 1.0/sqrt(t**2 + 1.0); s = t*c
        tau = s/(1.0 + c)
        temp = a[k,l]
        a[k,l] = 0.0
        a[k,k] = a[k,k] - t*temp
        a[l,l] = a[l,l] + t*temp
        for i in range(k):      
            temp = a[i,k]
            a[i,k] = temp - s*(a[i,l] + tau*temp)
            a[i,l] = a[i,l] + s*(temp - tau*a[i,l])
        for i in range(k+1,l):  
            temp = a[k,i]
            a[k,i] = temp - s*(a[i,l] + tau*a[k,i])
            a[i,l] = a[i,l] + s*(temp - tau*a[i,l])
        for i in range(l+1,n):  
            temp = a[k,i]
            a[k,i] = temp - s*(a[l,i] + tau*temp)
            a[l,i] = a[l,i] + s*(temp - tau*a[l,i])
        for i in range(n):      
            temp = p[i,k]
            p[i,k] = temp - s*(p[i,l] + tau*p[i,k])
            p[i,l] = p[i,l] + s*(temp - tau*p[i,l])        
    n = len(a)
    maxRot = 5*(n**2)       
    p = identity(n)*1.0     
    for i in range(maxRot): 
        aMax,k,l = maxElem(a)
        if aMax < tol: return diagonal(a),p
        rotate(a,p,k,l)
    print ('Jacobi method did not converge')
def convergence(arr, tolerance):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                continue
            else:
                if abs(arr[i][j]) > tolerance:
                    return False
    return True
def eigen_decomp_np(A, tolerance=1e-7):
    A_k = A.copy()
    m, n = A.shape
    Q_k = np.eye(n)
    i = 1    
    while(True):
        Q, R = np.linalg.qr(A_k)
        Q_k = Q_k @ Q
        A_k = R @ Q
        if(convergence(A_k, tolerance)):
            print("Number of iterations: " + str(i))
            break
        else:
            i += 1
    eigenvalues = np.diag(A_k)
    eigenvectors = Q_k
    return eigenvalues, eigenvectors  
A = np.array([[4.0,2.0,2.0,1.0],[2.0,-3.0,1.0,1.0],[2.0,1.0,3.0,1.0],[1.0,1.0,1.0,2.0]])
w1, v1 = eigen_decomp_np(A)
w, v = jacobi(A)
print(w1)

from numpy import array,identity,diagonal
from math import sqrt
import numpy as np

def jacobi(a,tol = 1.0e-9): 
    def maxElem(a): 
        n = len(a)
        aMax = 0.0
        for i in range(n-1):
            for j in range(i+1,n):
                if abs(a[i,j]) >= aMax:
                    aMax = abs(a[i,j])
                    k = i; l = j
        return aMax,k,l
    def rotate(a,p,k,l): 
        n = len(a)
        aDiff = a[l,l] - a[k,k]
        if abs(a[k,l]) < abs(aDiff)*1.0e-36: t = a[k,l]/aDiff
        else:
            phi = aDiff/(2.0*a[k,l])
            t = 1.0/(abs(phi) + sqrt(phi**2 + 1.0))
            if phi < 0.0: t = -t
        c = 1.0/sqrt(t**2 + 1.0); s = t*c
        tau = s/(1.0 + c)
        temp = a[k,l]
        a[k,l] = 0.0
        a[k,k] = a[k,k] - t*temp
        a[l,l] = a[l,l] + t*temp
        for i in range(k):     
            temp = a[i,k]
            a[i,k] = temp - s*(a[i,l] + tau*temp)
            a[i,l] = a[i,l] + s*(temp - tau*a[i,l])
        for i in range(k+1,l):  
            temp = a[k,i]
            a[k,i] = temp - s*(a[i,l] + tau*a[k,i])
            a[i,l] = a[i,l] + s*(temp - tau*a[i,l])
        for i in range(l+1,n):  
            temp = a[k,i]
            a[k,i] = temp - s*(a[l,i] + tau*temp)
            a[l,i] = a[l,i] + s*(temp - tau*a[l,i])
        for i in range(n):      
            temp = p[i,k]
            p[i,k] = temp - s*(p[i,l] + tau*p[i,k])
            p[i,l] = p[i,l] + s*(temp - tau*p[i,l])        
    n = len(a)
    maxRot = 5*(n**2)       
    p = identity(n)*1.0     
    for i in range(maxRot):  
        aMax,k,l = maxElem(a)
        if aMax < tol: return diagonal(a),p
        rotate(a,p,k,l)
    print ('Jacobi method did not converge')
def convergence(arr, tolerance):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                continue
            else:
                if abs(arr[i][j]) > tolerance:
                    return False
    return True
def eigen_decomp_np(A, tolerance=1e-7):
    A_k = A.copy()
    m, n = A.shape
    Q_k = np.eye(n)
    i = 1    
    while(True):
        Q, R = np.linalg.qr(A_k)
        Q_k = Q_k @ Q
        A_k = R @ Q
        if(convergence(A_k, tolerance)):
            print("Number of iterations: " + str(i))
            break
        else:
            i += 1
    eigenvalues = np.diag(A_k)
    eigenvectors = Q_k
    return eigenvalues, eigenvectors  

A = np.array([[4, 2, 1, 0, 0, 0, 0, 0, 0, 0],[2, 4, 2, 1, 0, 0, 0, 0, 0, 0],[1, 2, 4, 2, 1, 0, 0, 0, 0, 0],[0, 1, 2, 4, 2, 1, 0, 0, 0, 0],[0, 0, 1, 2, 4, 2, 1, 0, 0, 0],[0, 0, 0, 1, 2, 4, 2, 1, 0, 0],[0, 0, 0, 0, 1, 2, 4, 2, 1, 0],[0, 0, 0, 0, 0, 1, 2, 4, 2, 1],[0, 0, 0, 0, 0, 0, 1, 2, 4, 2],[0, 0, 0, 0, 0, 0, 0, 1, 2, 4]])
w1, v1 = eigen_decomp_np(A)
w, v = jacobi(A)
print(w1)