
n = int(raw_input().strip())
tel = {}
for i in range(0,n):
    users = raw_input()
    name =users.split()
    tel[str(name[0])] = str(name[1])
#print tel
lists = []
for i in range(0, n):
    lists.append(raw_input())
#print lists
for temp in lists:
    for k, v in tel.items():
        #print 'temp = ', temp
        #print 'compare',temp,k
        if temp == k:
            print k, v
            break
        print 'Not found'




