def DFS(L,sun):
    global cnt
    global k
    global T
    if sum > T: # 줄여줘야해
        return
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(coin_v[L]+1):  # 동전 갯수만큼 만약 5원이 3개면 0,1,2,3
            DFS(L+1,sum+(coin_k[L]*i))
        
T = int(input())
k = int(input())
coin_k = []
coin_v = []
cnt = 0
for _ in range(m):
    dong,d = map(int,input())
    coin_k.append(dong) # 종류
    coin_v.append(d)    # 갯수
DFS(0,0)
print(cnt)
