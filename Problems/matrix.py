import numpy as np
n=int(input("enter the matrix size: "))
matrix=np.random.randint(1,50,(n,n))
print("Before swapping matrix")
print(matrix)
for i in range(n):
    ls=matrix[i][i]
    rs=matrix[i][n - i - 1]
    matrix[i][i] =rs
    matrix[i][n - i - 1] =ls
print(matrix)