import numpy as np

a = np.array([[4, -4, 5, 0],
              [3, 5, 2, 1],
              [1, 1, 6, 1],
              [2, 3, 6, 5]],float)

b = np.array([7,2,4,5],float)

n = len(b)

x = np.zeros(n,float)

for k in range(n-1): 
    for i in range(k+1,n):
        if a[i,k] ==0:continue
        podziel = a[k,k]/a[i,k]
        for j in range(k,n):
            a[i,j] = a[k,j] - a[i,j]*podziel
        b[i] = b[k] - b[i]*podziel

print(a)
print(b)


x[n-1] = b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1):
    suma = 0
    for j in range(i+1,n):
        suma += a[i,j] * x[j]
    x[i] = (b[i]-suma)/a[i,i]

print(x)