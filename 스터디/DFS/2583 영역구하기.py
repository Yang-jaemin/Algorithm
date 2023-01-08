# # 슈도 코드
# #DFS 구현
# import sys
# sys.setrecursionlimit(10**6)
# def DFS(r,c):
#     global cnt,N,M
#     dx = [1,-1,0,0]
#     dy = [0,0,1,-1]
#     for v in range(4):
#         nx = c + dx[v]
#         ny = r + dy[v]
#         if 0 <= nx <= N-1 and 0<= ny <= M-1:
#             if A[ny][nx] == 0:
#                 cnt +=1
#                 A[ny][nx] = 1
#                 DFS(ny,nx)
#             else:
#                 continue
            
# # M,N(행,렬),K 받기
# M,N,K = map(int,input().split())
# # 원본[0]리스트 만들기
# A = [[0]* N for _ in range(M)]
# result = 0
# cnts = []
# cnt = 0
# # x1,y1,x2,y2 받고 원본리스트에 채우기
# for i in range(K):
#     x1,y1,x2,y2 = map(int,input().split())
#     for j in range(y1,y2):
#         for p in range(x1,x2):
#             A[j][p] = 1
# # DFS로 탐색

# for q in range(M):
#     for w in range(N):
#         if A[q][w] == 0:
#             A[q][w] = 1
#             cnt +=1
#             DFS(q,w)
#             result +=1
#             cnts.append(cnt)
#             cnt = 0
# cnts.sort()
# print(result)
# for z in cnts:
#     print(z,end = ' ')




# a = [[0]* 7 for _ in range(5)]

# x1, y1, x2, y2 = 0, 2, 4, 4

# for x in range(x1, x2):
#     for y in range(y1, y2):
#         a[y][x] = 1
# for e in a:
#     print(e)

# DFS 사용
def DFS(r,c):
    global mn
    dc = [1,-1,0,0]  # 사방을 봐야하니까 dc와 dr의 조합으로 동서남북 탐색 할 수 있도록
    dr = [0,0,1,-1]
    for i in range(4): # 4번 돌면서 동서남북 탐색
        nr = dr[i]+ r       
        nc = dc[i] + c
        if 0<= nr <= M-1 and 0 <= nc <= N-1:  # 범위안의 인덱스인지 확인하고
            if board[nr][nc] == 0:            # 0이라면
                board[nr][nc] = 1             # 1로 바꾼다
                mn += 1                       # 넓이 + 1
                DFS(nr,nc)                    # 그 부분에서 다시 DFS

import sys
sys.setrecursionlimit(10**6)

M,N,K = map(int,input().split())
board = [[0]*N for _ in range(M)]  # Board 판 제작
cnt = 0                            # 몇 덩어리인지
mns = []                           # 넓이를 append

for i in range(K):
    c1,r1,c2,r2 = map(int,input().split()) # 열,행 으로 주어져서 c1,r1 순으로 받음
    for i in range(r1,r2):
        for j in range(c1,c2):
            board[i][j] = 1        # 기존에 색칠되어있는 부분 색칠   -> board 완성
            
# for k in board:
#     print(k)
    
# [0, 0, 0, 0, 1, 1, 0]
# [0, 1, 0, 0, 1, 1, 0]
# [1, 1, 1, 1, 0, 0, 0]
# [1, 1, 1, 1, 0, 0, 0]
# [0, 1, 0, 0, 0, 0, 0]
            
for q in range(M):
    for p in range(N):
        if board[q][p] == 0:       # 0,0 부터 시작해서 끝까지 가는데 색칠 안되어있으면 DFS로 들어간다.
            mn = 1              
            board[q][p] = 1        # 시작지점 색칠해주고
            DFS(q,p)               # DFS 시작
            mns.append(mn)         # DFS에서 나온 넓이 append
            cnt += 1               # DFS에서 나왔다는 건 한덩이가 완성되었다는 뜻 cnt += 1
            
mns.sort() # 내림차순
# 출력
print(cnt)  
for mn in mns:
    print(mn,end = ' ')

    