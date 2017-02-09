#!/bin/python

import sys

#!/bin/python

def find_smalest(lists):
    return min(lists)

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

while arr:
    print len(arr)
    smallest = find_smalest(arr)
    actual_size = len(arr)
    i = 0
    while arr:
        if arr[i] - smallest ==0:
            del arr[i]
            actual_size-=1
        else:
            arr[i] = arr[i]-smallest
            i+=1
        if i == actual_size:
            break
