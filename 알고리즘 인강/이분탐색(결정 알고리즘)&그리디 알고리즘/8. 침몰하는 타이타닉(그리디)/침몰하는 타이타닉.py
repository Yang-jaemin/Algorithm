#deque 사용
from collections import deque
n,m = 4,100
weight = [70, 50, 80, 50]
weight.sort()
weight = deque(weight)
cnt = 0
while weight:
    if len(weight) ==1:
        cnt+=1
        break
        
    if weight[-1]+ weight[0] > m:
        weight.pop()
        cnt +=1
    else:
        weight.popleft() # 데크에서 사용가능 앞에 꺼를 빼준다 pop은 같음
        weight.pop()
        cnt += 1

print(cnt)


        
        