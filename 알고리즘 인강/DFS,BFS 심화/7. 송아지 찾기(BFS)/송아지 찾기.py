# BFS 는 레벨 탐색이다.  -> 큐(먼저 들어간게 먼저 나옴)
# 보통 최단거리가 뭐냐 할때 ㅇㅇ
from collections import deque
#슈도코드
# 입력 N,M
n,m = map(int,input().split())
# 좌표의 맥시멈
MAX = 10000
# check 변수
# 방문했을 때 체크하는거임
ch = [0]*(MAX+1)
# 거리 리스트
dis = [0]*(MAX+1) 
# n 이 처음 현수의 위치니까 체크 변수에서 체크 해야해
ch[n] = 1
# 처음 위치(n)은 거리가 0 이니까 초기화 해주고
dis[n] = 0
# dQ를 만들고 출발해야하니까 n을 append 해준다!
dQ = deque()
dQ.append(n)

# 보통 while 문으로 진행한다.
while dQ: # 비어있으면 끝
    now = dQ.popleft() # 일단 처음 시작지점을 큐에 넣는다
    if now == m:       # now가 도착하게된다면 탈출
        break
    for next in (now-1,now+1,now+5): # 세갈래로 뻗음
        if 0<next<=MAX:
            if ch[next] == 0:       # 아직 방문을 안했다면
                dQ.append(next)     # 큐에 넣고
                ch[next] = 1        # 방문했다고 체크하고
                dis[next] = dis[now]+1  # 거리계산 (어차피 now의 다음레벨이기 때문에 +1만 하면된다.)
print(dis[now])