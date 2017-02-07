#https://www.hackerrank.com/challenges/30-recursion

n = int(raw_input().strip())
def calc_factorial(x):
    if x ==1:
        return 1
    else:
        return (x * calc_factorial(x-1))

print calc_factorial(n)