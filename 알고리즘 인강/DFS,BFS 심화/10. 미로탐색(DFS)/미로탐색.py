from collections import deque
# 원본 리스트 받음
board = [list(map(int,input().split())) for _ in range(7)]
# 움직이기 위한 x,y
dx = [1,-1,0,0]
dy = [0,0,1,-1]
# 거리를 표시하기 위한 이차원 리스트
dis = [[0]*7 for _ in range(7)]
# BFS를 위한 큐 자료구조 만들어주고 큐에다가 처음 시작 좌표 넣어줘야헤
Q = deque()
Q.append((0,0)) # 튜플로
board[0][0] = 1 # 처음시작 = 방문처리 

while Q: # 큐가 차있으면 돈다
    tmp = Q.popleft() # 처음꺼 꺼내서
    for i in range(4):
        x = tmp[1]+dx[i]  # 사방으로 탐색
        y = tmp[0]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[y][x] == 0 :  # 범위안에 있고 방문한적이 없다면?
            board[y][x] =1                             # 방문했다고 표시하고
            dis[y][x] = dis[tmp[0]][tmp[1]]+1          # 거리 +1 하고
            Q.append((y,x))                            # 큐에 넣기 그래서 그 좌표 중심으로 4방 탐색할수있으니까
if dis[6][6]==0:        # 만약에 가로막혀서 끝에 도달하지 못했다면
    print(-1)
else:
    print(dis[6][6])   # 도착 했다면 출력
        