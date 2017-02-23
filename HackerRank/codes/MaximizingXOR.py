#https://www.hackerrank.com/challenges/maximizing-xor?
# utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

#Given two integers, L and R, find the maximal value of A xor B, where A and B satisfy the following condition:

# Complete the function below.

def maxXor(l, r):
    result = 0
    for i in range(l, r+1):
        for j in range(l, r+1):
            temp = i ^ j
            if temp > result:
                result = temp
    return result

_l = int(raw_input())
_r = int(raw_input())

res = maxXor(_l, _r)
print(res)
