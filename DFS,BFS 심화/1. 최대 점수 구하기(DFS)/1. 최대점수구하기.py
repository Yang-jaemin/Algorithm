# 부분집합을 구해주면 되는거자나
# 푼다 풀지 않는다 두갈래도 나가면서 1번 2번 3번 쭉 순서대로 처리해주면된다
# 그러면 DFS(L+1,total_t+T[L],total_s+S[L])  -> 이게 푼다
#      DFS(L+1,total_t,total_s)            -> 이게 안푼다
def DFS(L,total_t,total_s):
    global N,M,res
    if total_t > M:
        return
    if L == N:
        if total_s > res:
            res = total_s
        return
    
    else:
        DFS(L+1,total_t+T[L],total_s+S[L])
        DFS(L+1,total_t,total_s)
    
N,M = map(int,input().split())
S = [0]*N
T = [0]*N
check = [0]*N
res = -2147000000
for i in range(N):
    score,time = map(int,input().split())
    S[i] = score
    T[i] = time
DFS(0,0,0)
print(res)