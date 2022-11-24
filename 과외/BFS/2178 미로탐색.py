from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
n,m = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
dis = [[0]*m for _ in range(n)]
Q = deque()
board[0][0] = 0
Q.append((0,0))

while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[1]+dx[i]
        y = tmp[0]+dy[i]
        if  0 <= y <= n-1 and 0 <= x <= m-1 and board[y][x] == 1:
            board[y][x] = 0
            dis[y][x] = dis[tmp[0]][tmp[1]]+1
            Q.append((y,x))
print(dis[n-1][m-1]+1)
    