# 시간초과 - X 근데 출력은 맞음 시간초과는 왜나는거이무ㅜ
from collections import deque
T = int(input())
dx = [1,2,1,2,-1,-2,-1,-2]  # 나이트의 특성 반영
dy = [2,1,-2,-1,-2,-1,2,1]
for _ in range(T):
    n = int(input())
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    board = [[1]*n for _ in range(n)]
    dis = [[0]*n for _ in range(n)]
    board[y1][x1] = 0 # 시작지점
    Q = deque()
    Q.append((y1,x1))
    while Q:
        tmp = Q.popleft()
        for i in range(8):
            x = tmp[1] + dx[i]
            y = tmp[0] + dy[i]
            if 0<= x <= n-1 and 0 <= y <= n-1 and board[y][x] == 1:
                board[y][x] = 0
                dis[y][x] = dis[tmp[0]][tmp[1]] + 1
                Q.append((y,x))
                
    print(dis[y2][x2])