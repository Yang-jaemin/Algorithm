# 연결요소 = 엣지로 연결된 노드의 집합
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def DFS(v):  # 그냥 끝까지 도는거니까 종단 조건이 필요 x
    if visited[v] == 0:
        visited[v] = 1
        for z in A[v]:
            if visited[z] == 0:
                DFS(z)

n,m = map(int,input().split())
A = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0

for _ in range(m):  # 인접리스트 만드는 작업
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)
    
for x in range(1,n+1):
    if visited[x] == 0:
        DFS(x)
        cnt += 1
print(cnt)