from collections import deque
# 모르겠음
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dis = [[0]*m for _ in range(n)]
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]
Q = deque()
shark = list()

for y in range(n):
    for x in range(m):
        if board[y][x] == 1:
            shark.append((y,x))

for i in range(len(shark)):
    Q.append(shark[i])
    while Q:
        tmp = Q.popleft()
        for j in range(8):
            Y = tmp[0] + dy[j]
            X = tmp[1] + dx[j]
            if 0<= X <= m-1 and 0<= Y <= n-1 and board == 0:
                dis[Y][X] = dis[tmp[0]][tmp[1]]+1
                Q.append((Y,X))
print(dis)
    
    
            
            
        