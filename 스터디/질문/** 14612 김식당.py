# value error
n,m = map(int,input().split())
num = []
order = []
numm = []
for _ in range(n):
    a = input()
    if a[0] == 'o':
        order.append(int(a[6]))
        num.append((int(a[6]),int(a[8])))
        for v in order:
            print(v, end = ' ')
    elif a == 'sort':
        num.sort(key = lambda x: (x[1],x[0]))
        for i,j in num:
            numm.append(i)
            print(i,end = ' ')
    else:
        numm.remove(int(a[9]))
        if len(numm) != 0:
            for k in numm:
                print(k, end = ' ')
        else:
            print('sleep')
            
        
        