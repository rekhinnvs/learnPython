__author__ = 'rekhin'

#Find the difference in diagonal values of a square matrix

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
xSum=0
ySum=0
b = []
for i in range(0,n):
    b += a[i]
for i in range(0,n):
    xSum+=int(b[(i+1)*(n-1)])
    ySum+=int(b[i*(n+1)])
    #print "Y Sum : ",ySum
#print "X axis value : ",xSum
#print "Y axis value : ",ySum
print abs(xSum-ySum)
