# -*- coding: utf-8 -*-
"""
Get changes
@author: Yingzhi
"""

class Exchange:
    def countWays(self, changes, n, x):
        'return number of strategies to get x with changes'
        #denote dp[k][i]= number of solution with changes[i:] to get k
        #store those already computed
        s = [[0 for j in range(n+1)] for i in range(x+1)]
        for j in range(n+1):
            s[0][j] = 1
        for i in range(1,x+1):
            for j in range(n-1,-1,-1):
                if i-changes[j]<0:
                    s[i][j] = s[i][j+1]
                else:
                    s[i][j] = s[i][j+1]+s[i-changes[j]][j]   #don't use changes[j] or use at least one changes[j]
        return s[x][0]