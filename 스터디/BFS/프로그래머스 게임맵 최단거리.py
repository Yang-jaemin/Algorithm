from collections import deque

def solution(maps):
    c_len = len(maps[0])
    r_len = len(maps)
    distance = [[0]* c_len for _ in range(r_len)]
    Q = deque()
    
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    Q.append((0,0))
    distance[0][0] = 1
    maps[0][0] = 0 # 시작
    
    while Q:
        r,c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr <= r_len -1 and 0<= nc <= c_len -1:
                if maps[nr][nc] == 1 and distance[nr][nc] == 0:
                    maps[nr][nc] = 0
                    distance[nr][nc] = distance[r][c]+1
                    Q.append((nr,nc))
    
    if distance[r_len-1][c_len-1] == 0:
        return -1
    else:
        return distance[r_len-1][c_len-1]