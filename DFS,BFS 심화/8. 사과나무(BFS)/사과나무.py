# 슈도 코드
import sys
from collections import deque
# x 좌표 y 좌표 움직일거니까
dx = [1,-1,0,0]
dy = [0,0,1,-1]
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)] # 2차원 리스트
# 체크리스트
ch = [[0]*n for _ in range(n)]

# 여기에 합할거임
sum = 0

# 큐 만들어주기
Q = deque()
ch[n//2][n//2] = 1  # 처음 시작(방문)
sum += a[n//2][n//2] # 시작지점 값 더해주기
Q.append((n//2,n//2)) # 처음 시작지점 큐에 append 해주기
L = 0   # Level 0부터 시작

while True:
    if L == n//2: # 레벨이 끝까지 가려면 n//2 일때다
        break
    size = len(Q) # Q의 길이만큼(큐의 들어있는 개수만큼)
    
    for i in range(size): # size 만큼 돈다(큐에 들어가있는 만큼 돈다.)
        tmp = Q.popleft() # 앞에서부터 순서대로 나와서
        for j in range(4):  # 이 밑에 적용 -> 사방을 탐색
            x = tmp[1]+dx[j] # 열
            y = tmp[0]+dy[j] # 행
            if ch[y][x] == 0:   # 방문 안한곳만 가는거임
                sum+=a[y][x]
                ch[y][x] = 1    # 방문 했다고 표시
                Q.append((y,x)) # 맨뒤에 넣어
    L +=1 # 레벨 올려주기
print(sum)
            
    
    
    

