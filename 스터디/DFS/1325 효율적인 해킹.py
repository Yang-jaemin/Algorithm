# BFS 활용 (근데 시간초과)
# 1. 시작할 번호를 큐에 넣고 시작
# 2. 체크리스트 필요
# 3. while 문 들어가자마자 qq = Q.popleft()
# 4. 적당히 반복

from collections import deque
# BFS 
def BFS(start):
    cnt = 1         # 처음들어
    Q = deque()
    Q.append(start)
    visit = [0]*(n+1)  # 체크리스트
    visit[start] = 1
    
    while Q:
        qq = Q.popleft()
        
        for now in A[qq]:
            if visit[now] == 0:
                visit[now] = 1
                cnt += 1
                Q.append(now)
    
    return cnt
    

    
    
n,m = map(int,input().split())

A = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    A[b].append(a)

largest_cnt = 0
ans = []

for i in range(1,n+1):
    cnt = BFS(i)
    if cnt > largest_cnt:
        largest_cnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == largest_cnt:
        ans.append(i)

for z in ans:
    print(z,end = ' ')

        
    