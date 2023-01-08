# 예제는 다맞음
# 틀리기도하고 시간초과임
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def DFS(L,idx):
    global arrive
    if L == 5:
        arrive = True
        return
    else:
        if v[idx] == 0:
            v[idx] = 1
            for i in A[idx]:
                if v[i] == 0:
                    DFS(L+1,i)
            v[idx] = 0  # 일단 사용했으면 다시 0으로 되돌려놔야한다.
                    
                    



n,m = map(int,input().split())
A = [[] for _ in range(n+1)]
v = [0]*(n+1)
arrive = False
# 인접 리스트
for _ in range(m):
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)
    
for x in range(n):
    # v = [0]*(n+1)
    DFS(1,x)
    if arrive:
        break
if arrive:
    print(1)
else:
    print(0)
        

    
    