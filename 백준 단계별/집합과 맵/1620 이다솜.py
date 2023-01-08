import sys
n,m = map(int,sys.stdin.readline().split())
d1 = {}
d2 = {}
for i in range(n):
    a = input()
    d1[a] = i+1
    d2['i+1'] = a

for i in range(m):
    b = input()
    if b.isdigit():
        print(d2[b])
    else:
        print(d1[b])
        