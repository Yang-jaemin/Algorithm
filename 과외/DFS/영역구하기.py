# 슈도 코드
#DFS 구현
import sys
sys.setrecursionlimit(10**6)
def DFS(r,c):
    global cnt,N,M
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for v in range(4):
        nx = c + dx[v]
        ny = r + dy[v]
        if 0 <= nx <= N-1 and 0<= ny <= M-1:
            if A[ny][nx] == 0:
                cnt +=1
                A[ny][nx] = 1
                DFS(ny,nx)
            else:
                continue
            
# M,N(행,렬),K 받기
M,N,K = map(int,input().split())
# 원본[0]리스트 만들기
A = [[0]* N for _ in range(M)]
result = 0
cnts = []
cnt = 0
# x1,y1,x2,y2 받고 원본리스트에 채우기
for i in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(y1,y2):
        for p in range(x1,x2):
            A[j][p] = 1
# DFS로 탐색

for q in range(M):
    for w in range(N):
        if A[q][w] == 0:
            A[q][w] = 1
            cnt +=1
            DFS(q,w)
            result +=1
            cnts.append(cnt)
            cnt = 0
cnts.sort()
print(result)
for z in cnts:
    print(z,end = ' ')




# a = [[0]* 7 for _ in range(5)]

# x1, y1, x2, y2 = 0, 2, 4, 4

# for x in range(x1, x2):
#     for y in range(y1, y2):
#         a[y][x] = 1
# for e in a:
#     print(e)