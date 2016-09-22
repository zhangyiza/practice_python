# -*- coding: utf-8 -*-
"""
Number of strings
Get number of strings between s1, s2 with length [len1, len2] with dict order
@author: Yingzhi
"""
while True:
    try:
        #字典序：从左往右比较，空<'a'<'b'<...，不同则必出大小，一样则比较后一位
        s1,s2,len1,len2 = raw_input().split(' ')
        len1 = int(len1)
        len2 = int(len2)
        #要保证s1<=s2算法才有效，所以先对s1>s2的print结果为0
        if s1>s2:
            print 0
        else:
            sum = 0
            last = 0
            for i in range(len2):
                #对于前i-1字符在s1,s2中间的，已经分出大小，第i个字符随便什么都可以
                current = last*26
                #对于前i-1个字符=s1的（len(s1)<i-1个时这种情况不存在），(s1<=s2)
                    #1）若s2[i]是最后一个，第i个字符>s1[i]且<s2[i]即可
                    #2）若s2[i]不是最后一个，第i个字符>s1[i]且<=s2[i]即可
                    #注意s2[i]可能为空，这时候没有可行的s1[i]可能为空，这时候所有字母都大于它
                if len(s1)>=i and len(s2)>=i+1:  #len(s1)>=i且s2[i]不为空
                    if len(s2) == i+1:  #s2[i]是最后一个
                        if len(s1) == i:  #s1[i]为空
                            current = current + (ord(s2[i])-1)-(ord('a')-1)
                        else:
                            current = current + (ord(s2[i])-1)-ord(s1[i])
                    else:
                        if len(s1) == i:  #s1[i]为空
                            current = current + ord(s2[i])-(ord('a')-1)
                        else:
                            current = current + ord(s2[i])-ord(s1[i])
                #从len1开始累加进sum
                if i>=len1-1:
                    sum = sum + current
                last = current
            print sum
    except:
        break
