# 2667 실패 런타임 에러(recursion Error)
def DFS(y,x):
    global n                
    global cnt
    dx = [1,-1,0,0]   # 상하좌우 움직임 고려
    dy = [0,0,1,-1]   # 상하좌우 움직임 고려
    for q in range(4):
        nx = x + dx[q]
        ny = y + dy[q]
        if 0<= nx <= n-1 and 0 <= ny <= n-1: # 차례로 탐색
            if check_map[ny][nx] == 1:
                cnt=+1
                check_map[ny][nx] = 0
                DFS(ny,nx)
            else:
                continue

n = int(input())                        # 1. n x n 인지 입력
check_map = [[0]*n for _ in range(n)]   # 2. n x n 을 0으로 채움
a = ''                                  # 3. 숫자를 붙여서 받아서 문자열로 받음
b = []                                  # 4. 각 덩이마다 나오는 cnt를 b에 append 한다음 sorting 해서 출력할 예정
cnt = 0
for i in range(n):
    a = input()
    for j in range(n):
        check_map[i][j] = int(a[j])     # 5. 문자열로 받아서 check_map 안에 숫자를 넣어줌

for y in range(n):                      # 6. 이제 탐색 행->열 순서
    for x in range(n):
        if check_map[y][x] == 1:        # 7. 만약 1이 들어가있으면
            cnt+=1                      # 8. 개수를 하나 세고
            check_map[y][x] = 0         # 9. 0으로 바꾼다음에
            DFS(y,x)                    # 10. 사방을 탐지 (사방을 탐지하면서 개수를 센다)
            b.append(cnt)               # 11. 개수 다세면 그거를 b에 append한다.
            cnt = 0                     # 12. 다음 덩어리에서 다시 써야하니 cnt를 0으로 초기화
        else: 
            continue
b.sort()
for x in b:
    print(x)
        
    