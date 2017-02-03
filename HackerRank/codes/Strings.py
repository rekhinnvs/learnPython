#Hacker rank day 6
#https://www.hackerrank.com/challenges/30-review-loop?h_r=next-challenge&h_v=zen

n = int(raw_input().strip())
names = []
for i in range(0, n):
    names.append(raw_input())
for i in range(0, n):
    restructured = names[i]
    output_second = output_first = ''
    for j in range(0,len(restructured)):
        if(j%2==0):
            output_first = output_first+restructured[j]
        else:
            output_second = output_second+restructured[j]
    print output_first, output_second
