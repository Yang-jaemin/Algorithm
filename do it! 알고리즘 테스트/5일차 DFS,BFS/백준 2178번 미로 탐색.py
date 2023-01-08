# 미로탐색
from collections import deque
def BFS(r,c):
    Q.append((r,c)) # 넣었으니까 방문 처리
    visit[r][c] = 1
    while Q:
        qq = Q.popleft()
        for k in range(4):
            nr = qq[0] + dr[k]
            nc = qq[1] + dc[k]
            if 0<= nr <= n-1 and 0<= nc <= m-1:
                if A[nr][nc] == 1 and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    A[nr][nc] = A[qq[0]][qq[1]]+1
                    Q.append((nr,nc))


dr = [0,1,0,-1]
dc = [1,0,-1,0]

n,m = map(int,input().split())
A = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]
Q =  deque()

for i in range(n):  # 리스트를 정수로 넣어주는거야
    a = list(input())
    for j in range(m):
        A[i][j] = int(a[j])
        
BFS(0,0)
print(A[n-1][m-1])

