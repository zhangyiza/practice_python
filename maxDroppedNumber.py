# -*- coding: utf-8 -*-
"""
Max dropped number
@author: Yingzhi
drop n numbers of l to get max integer
"""

l = map(int, list(raw_input()))   #original integer(can be very large)
n = int(raw_input())    #number of dropped numbers


remain = n
out = []
while remain>0 and l != []:
    to = min(remain+1, len(l))
    max_ix = max(range(to), key = lambda i: l[i])
    out.append(l[max_ix])
    remain = remain-max_ix
    l = l[max_ix+1:]
if remain != 0:
    out = out[:-remain]
elif l != []:
    out.extend(l)
print ''.join(map(str, out))

