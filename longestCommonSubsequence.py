# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:32:18 2016
A, B's longest common subsequence 公共子序列（可以不连续，abc,a2b3c=>3）
@author: Yingzhi
"""

def findLCS(A, n, B, m):
    #l(i,j)是两个串的最长公共子序列的长度
    l = [[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1]==B[j-1]:
                l[i][j] = 1+l[i-1][j-1]
            else:
                l[i][j] = max(l[i][j-1], l[i-1][j])
    return l[n][m]