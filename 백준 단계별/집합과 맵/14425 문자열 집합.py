import sys
n,m = map(int,sys.stdin.readline.split())
d = {}
cnt = 0
for _ in range(n):
    a = input()
    d[a] = 0

for _ in range(m):
    b = input()
    if b in d:
        cnt += 1
print(cnt)
