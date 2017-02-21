n = int(raw_input())
data = []
for i in range(0,n):
	data[i] = int(raw_input())
for i in data:
	row = i%2
	column = i/2
	print row*column
