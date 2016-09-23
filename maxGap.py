# -*- coding: utf-8 -*-
"""
Max gap
@author: Yingzhi

"""

class MaxGap:
    def findMaxGap(self, A, n):
        '''
        get max abs(left max - right max) splitting A somewhere
        Strategy:
            max(A) must be chosen.
            abs(max(A)-left max) can't be larger than abs(A[0]-m))
            abs(max(A)-right max) can't be larger than abs(m-A[n-1])
        '''
        m = max(A)
        return max(abs(A[0]-m), abs(m-A[n-1]))