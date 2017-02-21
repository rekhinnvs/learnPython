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
