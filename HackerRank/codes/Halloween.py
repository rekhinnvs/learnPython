#Alex is attending a Halloween party with his girlfriend, Silvia. At the party, Silvia spots the corner of an infinite chocolate bar (two dimensional, infinitely long in width and length).
#If the chocolate can be served only as 1 x 1 sized pieces and Alex can cut the chocolate bar exactly k times, what is the maximum number of chocolate pieces Alex can cut and give Silvia?

n = int(raw_input())
data = []
for i in range(0,n):
    data.append(int(raw_input()))
for i in data:
    row = i/2
    print 'row', row
    column = i-row
    print 'column', column
    print row*column
