# 큐: 뒤로 넣고 앞에서 뺀다. 입출구가 다르다.
from collections import deque
n , k =8,3
dq = list(range(1,n+1)) # 리스트
dq = deque(dq) # 데큐
while dq:
    for _ in range(k-1):    # 3번째 사람을 제거해야하니까 앞의 두사람은 빼서 뒤로 보냄
        cur = dq.popleft()  # 앞에서 빼서
        dq.append(cur)      # 뒤로 보냄
    dq.popleft()
    
    if len(dq) == 1:
        print(dq[0])
        dq.pop()
