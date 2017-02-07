
n = int(raw_input().strip())
tel = {}
for i in range(0,n):
    users = raw_input()
    name =users.split()
    tel[str(name[0])] = str(name[1])
lists = []
for i in range(0, n):
    lists.append(raw_input())
for temp in lists:
    if temp in tel.keys():
        print temp+'='+tel[temp]
    else:
        print 'Not found'




