import numpy as np
import sys

sys.stdin =open('input2.txt','r')
n = int(input())
a = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        a[i][j] = float(input())

x=np.ones(shape=(n,1))
tolerable_error = float(input())
max_iteration = int(input())
print('entered matrix is')
print (a)
print('\n')
print('Entered tolerable error: ',tolerable_error)
print('\n')
lambda_old = 1.0
condition = True
step = 1
while condition:
    x = np.matmul(a,x)
    lambda_new = max(abs(x)) 
    x = x/lambda_new
    print ('\nIteration %d' %(step))
    print ('----------')
    print ('Eigen Value = %0.6f' %(lambda_new))
    print ('Eigen Vector: ',x,sep='\n')
    step = step + 1
    if step > max_iteration:
        print ('Not convergent in given maximum iteration!')
        break
    error = abs(lambda_new - lambda_old)
    print ('error='+ str(error))
    lambda_old = lambda_new
    condition = error > tolerable_error

