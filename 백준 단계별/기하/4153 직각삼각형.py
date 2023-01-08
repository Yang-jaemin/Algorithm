A = []
while True:
    a,b,c = map(int,input().split())
    A.append(a)
    A.append(b)
    A.append(c)
    A.sort()
    if a+b+c == 0:
        break
    
    if A[2]**2 == A[1]**2+A[0]**2:
        print('right')
    else:
        print('wrong')
    A = []