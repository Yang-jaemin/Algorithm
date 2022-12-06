import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def DFS(L,idx):
    global arrive
    if L == 5:
        arrive = True
    else:
        if v[idx] == 0:
            v[idx] = 1
            for i in range(n):
                if A[idx][i] == 1 or A[i][idx] == 1:
                    DFS(L+1,i)
                    
                    



n,m = map(int,input().split())
A = [[0]*n for _ in range(n)]
v = [0]*n
arrive = False
# 인접행렬
for _ in range(m):
    s,e = map(int,input().split())
    A[s][e] = A[e][s] = 1
for x in range(n):
    DFS(0,x)
    if arrive:
        print(1)
        break
    else:
        print(0)

    
    