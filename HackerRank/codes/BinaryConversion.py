#https://www.hackerrank.com/challenges/30-binary-numbers

n = int(raw_input().strip())
result = ""
while True:
    result = result + str(n % 2)
    if (n==1):
        break
    n = n / 2
# reverse a string print result[::-1]
x=0
while True:
   if



