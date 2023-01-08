# 왜안되냐??
import sys
n,m = map(int,sys.stdin.readline().split())
d = {}
answer = []
cnt = 0 
for i in range(n):
    a = sys.stdin.readline()
    d[a] = 0

for j in range(m):
    b = sys.stdin.readline()
    if b in d:
        d[b] = 1
        cnt += 1
        answer.append(b)
print(cnt)
for z in answer:
    print(z,end = '')
