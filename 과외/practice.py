cnt = 0
n,m = map(int,input().split())
A = dict()
s = list(input() for _ in range(n))
for c in s:
        A[c] = 0
e = list(input() for _ in range(m))
for a in e:
    if a in A:
        cnt +=1
print(cnt)
