__author__ = 'rekhin'


import sys


n = int(raw_input().strip())
a = b = c = 0
arr = map(int, raw_input().strip().split(' '))
for i in range(0,n) :
    if arr[i] >= 0 :
        if arr[i] == 0 :
            b += 1
        else :
            a+=1
    else :
        c+=1

print float(a)/n
print float(c)/n
print float(b)/n
