#!/bin/python

def find_smalest(lists):
    return min(lists)

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
while arr:
    smallest = find_smalest(arr)
    print 'smallest value ',smallest
    print 'Lenght of array ', len(arr)
    for index, value in enumerate(arr):
        temp = value - smallest
        #print 'value',value
        #print 'temp', temp
        if temp == 0:
            del arr[index]
        else:
            arr[index] = temp
    print 'array after 1 iteration', arr

