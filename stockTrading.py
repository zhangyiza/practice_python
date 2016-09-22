# -*- coding: utf-8 -*-
"""
Stock trading
@author: Yingzhi
"""
class Stock:
    def maxProfit(self, prices, n):
        '''
        假设最多可进行两次买卖(即买和卖的次数均小于等于2)
        规则是必须一笔成交后进行另一笔(即买-卖-买-卖的顺序进行)
        给出一天中的股票变化序列pieces，得到一天可以获得的最大收益
        '''
        #思路：遍历从不同位置分割prices，两边分别进行两次交易的总收益
        #问题变成了求0到k和k+1到n-1的数组的max(0, 最大差值（有序）)的问题（不交易的时候取0，也可以看做当天买卖）
        if n<2:
            return 0
        # left[k]=price[:k+1]'s max pj-pi(j>i)
        # right[k]=price[k:]'s max pj-pi(j>i)
        left = [0 for i in range(n)]
        for k in range(1,n):  #compute left[k]
            tmp = prices[k]-min(prices[:k])
            left[k] = max(tmp, left[k-1])
        right = [0 for i in range(n)]
        for k in range(n-2,-1,-1):  #compute right[k]
            tmp = max(prices[k+1:])-prices[k]
            right[k] = max(tmp, right[k+1])

        # find the best place to split price and get max r[k] = left[k]+right[k+1]
        best = 0
        for i in range(n-1):
            best = max(left[i]+right[i+1], best)
        return best