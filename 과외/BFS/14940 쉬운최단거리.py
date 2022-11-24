import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]     # BFS가 사방으로 뻗을거니까
dy = [0,0,1,-1]
# 입력
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
# 거리를 저장할 2차원 리스트
dis = [[0]*m for _ in range(n)]

# 큐생성
Q = deque()

# 시작지점 세팅 (board에서 2라고 되어있는 부분이 시작지점)
for r in range(n):
    for c in range(m):
        if board[r][c] == 2:
            board[r][c] = 0
            Q.append((r,c))

# BFS 시작
while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[1]+dx[i] # 열
        y = tmp[0]+dy[i] # 행
        if 0<= x <= m-1 and 0<= y <= n-1 and board[y][x] == 1:
            board[y][x] = 0
            dis[y][x] = dis[tmp[0]][tmp[1]]+1 # 어차피 사방으로 1번 간거니까 그전 거리(dis[바뀌기전y][바뀌기전x] 에서 +1을 하면된다.
            Q.append((y,x))   # 큐에 넣어주기 -> 계속 반복
            
for r1 in range(n):
    for c1 in range(m):
        if board[r1][c1] == 1:   # BFS가 끝났는데도 0으로 안바뀌어있다? 그러면 못가는 곳이니까 -1
            dis[r1][c1] = -1

for r2 in dis:
    for c2 in r2:  # 출력
        print(c2,end = ' ')
    print() 
    