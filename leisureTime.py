# -*- coding: utf-8 -*-
"""
Leisure time
@author: Yingzhi
A的空闲时间为[a1 ,b1 ],[a2 ,b2 ]..[ap ,bp ]。
B的空闲时间是[c1 +t,d1 +t]..[cq +t,dq +t],t为B的起床时间。
B的起床时间为[l,r]的一个时刻。
若一个起床时间能使两人在任意时刻聊天，那么这个时间就是合适的。
问有多少个合适的起床时间？
"""

while True:
    try:
        p, q, l, r = map(int, raw_input().split(' '))
        a = []
        b = []
        c = []
        d = []
        for i in range(p):
            m, n = map(int, raw_input().split(' '))
            a.append(m)
            b.append(n)
        for i in range(q):
            m, n = map(int, raw_input().split(' '))
            c.append(m)
            d.append(n)
        count = 0
        t = l
        while t<=r:
            flag = 0
            for i in range(q):  #i: A's ith leisure
                b_begin = t+c[i]
                b_end = t+d[i]
                for j in range(p):  #j: B's jth leisure
                    a_begin =  a[j]
                    a_end = b[j]
                    if (b_end>=a_begin and b_end<=a_end) or (b_begin>=a_begin and b_begin<=a_end):
                        #if b_end or b_begin in [a_begin, a_end], t verified and move to the next t(break 2 loops)
                        count = count+min(a_end-b_begin+1,r-t+1)
                        t = t+a_end-b_begin+1
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 0:
                t = t+1
        print count
    except EOFError:
        break