#https://www.hackerrank.com/challenges/compare-the-triplets

#!/bin/python

import sys


a0, a1, a2 = raw_input().strip().split(' ')
a = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b = [int(b0), int(b1), int(b2)]
al = bl =0
for i in range(0, len(a)):
    for j in range(0, len(b)):
        if i > j:
            al = 1
            break
        elif i < 0:
            bl = 1
            break
        else:
            break
print al, bl
