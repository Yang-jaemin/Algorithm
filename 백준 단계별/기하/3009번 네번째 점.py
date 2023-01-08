a = []
dx = {}
dy = {}
for _ in range(3):
    x,y = map(int,input().split())
    if x not in dx:
        dx[x] = 1
    else: 
        dx[x] += 1
    if y not in dy:
        dy[y] = 1
    else: 
        dy[y] += 1
for k,v in dx.items():
    if v ==  1:
        print(k,end = ' ')
for k,v in dy.items():
    if v ==  1:
        print(k,end = ' ')