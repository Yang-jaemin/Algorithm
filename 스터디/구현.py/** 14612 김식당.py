n,m = map(int,input().split())
num = []
for i in range(m):
    a = input()
    num.append((a[8],a[6]))
    for x in range(i+1):
        print(num[i][0])

for _ in range(n-m):
    b = input()
    if b == 'sort':
        num.sort()
    else:
