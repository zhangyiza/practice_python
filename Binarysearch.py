# -*- coding: utf-8 -*-
"""
BinarySearch：返回某个数是否存在于一个有序列表
@author: Yingzhi
"""

def bs(d, s, left, right):
    'get if s is in d[left] to d[right](inclusive)'
    if left>right:
        return False
    else:
        mid = (left+right)//2
        if d[mid] == s:
            return True
        elif d[mid] <s:
            return bs(d, s, mid+1, right)
        else:
            return bs(d, s, left, mid-1)

def binary_search(d, s):
    return bs(d, s, 0, len(d)-1)