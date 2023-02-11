# 1시간
from collections import deque
def BFS(arr):
    start = []
    for i in range(5): # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if arr[i][j] == 'P':
                start.append((i, j))
    if len(start) == 0:
        return 1
    
    for s in start:
        Q = deque() 
        Q.append(s)    # 큐 초기값
        visited = [[0]*5 for _ in range(5)]   # 방문 처리 리스트
        distance = [[0]*5 for _ in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1 # visited[i][j] = 1
        K = 10
        
        while Q:
                r, c = Q.popleft()
        
                dc = [-1, 1, 0, 0]  # 열
                dr = [0, 0, -1, 1]  # 행

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0<=nr<5 and 0<=nc<5 and visited[nr][nc] == 0:
                    
                        if arr[nr][nc] == 'O':
                            Q.append((nr, nc))
                            visited[nr][nc] = 1
                            distance[nr][nc] = distance[r][c] + 1
                    
                        if arr[nr][nc] == 'P' and distance[r][c] < 2:
                            return 0
    return 1
    
def solution(places):
    answer = []
    for group in places:
        answer.append(BFS(group))
    return answer
            
#   *
#  ***
# **o**
#  ***
#   *
   
# 000xx
# x000x
# 000xx
# 0x00x
# 00000


# xxxxxxxxx
# xxxxxxxxx
# xx000xxxx
# xxx000xxx
# xx000xxxx
# xx0x00xxx
# xx00000xx
# xxxxxxxxx
# xxxxxxxxx

def sol(pl):
    R = len(pl)
    C = len(pl[0])
    
    # 벽 두 겹 둘러치기(Sentinel)
    for i in range(R):
        pl[i] = 'XX' + pl[i] + 'XX'
    pl = ['X'*(C+4)] + ['X'*(C+4)] + pl + ['X'*(C+4)] + ['X'*(C+4)]

    #print("=====================")
    #for x in pl:
    #    print(x)
    for r in range(R+4):
        for c in range(C+4):
            if pl[r][c] != 'P':
                continue
                # 동서남북
            if pl[r+1][c] == 'P' or pl[r-1][c] == 'P' or pl[r][c+1] == 'P' or pl[r][c-1] == 'P':
                return 0
                # 2칸떨어짐
            if pl[r+2][c] == 'P' and pl[r+1][c] == 'O':
                return 0
            if pl[r-2][c] == 'P' and pl[r-1][c] == 'O':
                return 0
            if pl[r][c+2] == 'P' and pl[r][c+1] == 'O':
                return 0
            if pl[r][c-2] == 'P' and pl[r][c-1] == 'O':
                return 0
                # 대각선
            if pl[r+1][c+1] == 'P' and (pl[r+1][c] == 'O' or pl[r][c+1] == 'O'):
                return 0
            if pl[r+1][c-1] == 'P' and (pl[r+1][c] == 'O' or pl[r][c-1] == 'O'):
                return 0
            if pl[r-1][c+1] == 'P' and (pl[r-1][c] == 'O' or pl[r][c+1] == 'O'):
                return 0
            if pl[r-1][c-1] == 'P' and (pl[r-1][c] == 'O' or pl[r][c-1] == 'O'):
                return 0
    return 1
    
def solution(places):
    answer = [sol(pl) for pl in places]
    return answer