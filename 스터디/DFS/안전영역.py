# 실패(예제 입력은 통과 -> 채점해보면 recursion Error가 나옴)
# 이게 있으니까 맞음 ㅋㅋㅋ
import sys
sys.setrecursionlimit(10**6)

def DFS(Y,X):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = X + dx[i]
        ny = Y + dy[i]
        if 0<= nx <= n-1 and 0<= ny <= n-1:    # 바운더리 안에 들어오면 실행
            if check_map[ny][nx] == 1:         # 만약 1이면(사방) 0으로 바꾸고 다시 사방탐지
                check_map[ny][nx] = 0
                DFS(ny,nx)
            else:
                continue
def mmax(li):    # 리스트에서 가장 큰 값 찾는 함수
    b = []
    for i in li:
        b.append(max(i))
    return max(b)  
    
n = int(input())                                                # 1. n X n 행렬
og_map = [list(map(int,input().split())) for _ in range(n)]     # 2. 행렬 값 입력
check_map = [[0]*n for _ in range(n)]                           # 3. 장마왔을때 넘치는지 안넘치는지 체크위한 n X n (넘친다면 0 안넘친다면 1)
cnt = 0
res = []
for a in range(mmax(og_map)+2):                                 # 4. 비가 오는 양 (0부터 젤큰값(리스트안에서))
    for i in range(n):
        for j in range(n):
            if og_map[i][j] >= a:                               # 5. 만약 비가오는 양보다 크거나 같다면 1(안넘침) -> check_map
                check_map[i][j] = 1
            else:
                check_map[i][j] = 0                             # 6. 작다면 0(넘침)-> check_map
            
    for y in range(n):
        for x in range(n):
            if check_map[y][x] == 1:                            # 7. check_map 탐색 -> 만약 1이면 0으로 바꾸고
                check_map[y][x] = 0
                DFS(y,x)                                        # 8. 사방을 탐색(덩어리 탐색)
                cnt+=1                                          # 9. 덩어리를 모두 0으로 만들고 탈출(cnt =+1)
    res.append(cnt)                                             # 10. 다 탐색후 cnt(덩어리 갯수)를 res에 append (cnt가 가장 큰경우를 찾아야해서)
    cnt = 0
    for z1 in range(n):
        for z2 in range(n):
            check_map[z1][z2] = 0                               # 11. 비가 오는 양에 따라 check_map이 달라지니까 다시 0으로 초기화
            
print(max(res))        