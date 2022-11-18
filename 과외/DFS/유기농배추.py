# 실패 1012
# 틀림 -> 맞춤
import sys
sys.setrecursionlimit(10**6) # 이게 있어야함

def DFS(i,j):
    global M
    global N
    dx = [1,-1,0,0] # 상하좌우 탐색하기위해서 dx dy 만듬
    dy = [0,0,1,-1]
    for p in range(4):
        nx = j + dx[p]
        ny = i + dy[p]
        if 0<= nx <= M-1 and 0 <= ny <= N-1: # 2차원 행렬 범위밖에 나가면 종료 # 종단조건이라고 할 수있음
            if check_map[ny][nx] == 1:             # 만약에 1이면   
                check_map[ny][nx] = 0              # 0으로 바꾸고 사방을 탐색
                DFS(ny,nx)
            else:
                continue
                
T = int(input())    # 1. 2개의 테스트 케이스
for _ in range(T):  # 2. 2개의 테스트 케이스 입력
    M,N,K = map(int,input().split()) # 3. 열, 행, 배추 갯수 순으로 입력
    cnt = 0                          
    check_map = [[0]* M for _ in range(N)]  # 4. M열 N행의 맵 만듬
    
    for _ in range(K):
        X,Y = map(int,input().split()) # 5. 받은 좌표에 1을 집어 넣음(배추 어디에 있나 표시)
        check_map[Y][X] = 1
    
    for i in range(N): # 행        
        for j in range(M): # 열
            if check_map[i][j] == 1:  # 6. 0행 0열 -> 0행 1열 순으로 좌표에 1이 들어가 있나 확인
                check_map[i][j] = 0
                DFS(i,j)        # 7. 만약 들어가있다면 DFS 실행
                cnt+=1          # 8. DFS에서 탈출할 경우 결국 덩어리 하나가 끝난거 일테니까 cnt에 +1
            else: 
                continue        # 9. map에 1이 들어가있지 않다면 continue 하고 다음거 탐색
    print(cnt)                  # 10. 탐색 끝나면 cnt 출력
