# -*- coding: utf-8 -*-
"""
Product matrix
@author: Yingzhi
A[n,m]是一个n行m列的矩阵，a[i,j]表示A的第i行j列的元素，定义x[i,j]为A的第i行和第j列除了a[i,j]之外所有元素(共n+m-2个)的乘积，即x[i,j]=a[i,1]*a[i,2]*...*a[i,j-1]*...*a[i,m]*a[1,j]*a[2,j]...*a[i-1,j]*a[i+1,j]...*a[n,j],现输入非负整形的矩阵A[n,m]，求MAX(x[i,j])，即所有的x[i,j]中的最大值。
"""

#input
n, m = map(int, raw_input().split(' '))
A = []
for i in range(n):
    A.append(map(int, raw_input().split(' ')))

#get matrix R and C = product of row/col without self
def product(A):
    'get row product without self with dp'
    P = []
    for i in range(len(A)):   #row A[i]
        #product_left[k] = product of left elements of A[i][k]
        prodect_left = [1 for k in range(len(A[i]))]
        for j in range(1,len(A[i])):     #each col
            prodect_left[j] = A[i][j-1]*prodect_left[j-1]
        prodect_right = [1 for k in range(len(A[i]))]
        for j in range(len(A[i])-2,-1,-1):     #each col
            prodect_right[j] = A[i][j+1]*prodect_right[j+1]
        product_row = [prodect_left[k]*prodect_right[k] for k in range(len(A[i]))]
        P.append(product_row)
    return P

R = product(A)
#C can be computed by trasform of A
A_T = zip(*A)
C = zip(*product(A_T))

#get max x[i,j] = C[i][j]*R[[i][j]
largest = 0
for i in range(n):
    for j in range(m):
        largest = max(C[i][j]*R[i][j], largest)
print largest
