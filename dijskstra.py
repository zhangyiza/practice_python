# -*- coding: utf-8 -*-
"""
Directed graph shortest path: dijskstra
get shortest path prepoint and length from some point to all others
@author: Yingzhi
"""

def dijskstra(s, d, n):
    '''
    return
        L = list of shortest length from s to all points(None for no path)
        pre = list of shortest path pre_point(None for no path)
    s is starting point(0 or 1 or 2..)
    d is point*point distance matrix
        points are 0,1,2..,d[i][j] is edge length from i to j, no edge is inf
        len(d) is number of points
    '''
    global inf
    #initial L: list to store shortest distance from s to all points
    L = [d[s][i] for i in range(n)]
    #initial pre: list to store pre point
    pre = [None for i in range(n)]
    for i in range(n):
        if d[s][i] != inf:
            pre[i] = s
    #initial V: visited point set(L is shortest); U: unvisited point set
    V = set([s])
    U = set(range(n))
    U.remove(s)
    while len(U)!=0:    #U is not null
        #choose point with min(L(point)) in U
        point = min(U, key = lambda i: L[i])
        #L(point) must be the shortest distance of point
        V.add(point)
        U.remove(point)
        #update L(U)
        for i in U:
            tmp = L[point]+d[point][i]
            if tmp < L[i]:
                L[i] = tmp
                pre[i] = point
    #=inf mean can't reach
    for i in range(n):
        if L[i] == inf:
            L[i] = None
    return L, pre

#config
inf = 10000 #larger than longest path from s(eg. sum of edge length)
n = 6    #number of points, points must be 0, 1, 2 ...
edges = [[0,1,5],[0,2,8],[1,4,30],[2,4,10]]   #edges = list of [(int)point_from, (int)point_to, (int)length]
s = 0  #starting point
#get distanve matrix
d = [[inf for j in range(n)] for i in range(n)]
for i in range(n):
    d[i][i] = 0
for edge in edges:   #edge = [point_from, point_to, length]
    d[edge[0]][edge[1]] = edge[2]
#get shortest length
L,pre = dijskstra(s,d,n)