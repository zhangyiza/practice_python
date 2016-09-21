# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:28:17 2016
A, B's longest common substring 最大公共子串（不能断），O(m*n)
@author: Yingzhi
"""

def findLongest(self, A, n, B, m):
        # write code here
        #l(i,j)是以A[i]和B[j]开头的最长公共串的长度
        #longest = max l(i,j)
        l = [[0 for j in range(m+1)] for i in range(n+1)]   #note: 不能 [[0]*(m+1)]*(n+1)！会共享一些数值地址。。导致修改l[16][2]会改所有l[*][2]。。。
        #注意：虚拟边界：i=n or j = m，l(n,)=l(,m)=0
        longest = 0
        for i in range(n-1,-1,-1):   #n-1,...,1,0
            for j in range(m-1,-1,-1):   #m-1,...,1,0
                if A[i]==B[j]:
                    l[i][j] = 1+l[i+1][j+1]
                    #find max l(i,j)
                    if l[i][j]>longest:
                        longest = l[i][j]
                else:
                    l[i][j] = 0
        return longest