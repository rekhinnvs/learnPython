__author__ = 'rekhin'

import sys

n = int(raw_input().strip())
for i in range(1, n+1):
    x = n-i
    while x>0:
        sys.stdout.write(" "),
        x = x-1
    for j in range(0,i):
        sys.stdout.write("#"),
    print