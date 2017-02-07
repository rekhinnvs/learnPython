# Complete the function below.


def StairCase(n):
    extra_space = n - 1
    for i in range(1, n+1):
        for j in range(0, extra_space):
            print ' ',
        for k in range(0, i):
            print '#',
        print
        extra_space -= 1

n = int(raw_input())
StairCase(n)
