def DFS(L):
    global minn
    global n
    if L == n:
        if minn > max(abc)-min(abc):
            tmp = set()
            for v in abc:
                tmp.add(v)
            if len(abc) == len(tmp):
                minn = max(abc)-min(abc)
    else:
        for j in range(3):
            abc[j] = abc[j] + w[L] 
            DFS(L+1)
            abc[j] = abc[j] - w[L]
        


n = int(input())
w = []
minn = 2147000000
abc = [0]*3
for _ in range(n):
    a = int(input())
    w.append(a)
DFS(0)
print(minn)