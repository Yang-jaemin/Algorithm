# 못품, 구현을 못하겠음
# from collections import deque
# n,w,L = map(int,input().split())
# truck = deque(map(int,input().split()))
# on_bridge = deque()
# on_bridge.append(truck.popleft())
# cnt = 1
# while truck:
#     to_bridge = truck.popleft()
#     if sum(on_bridge)+ to_bridge > L:
#         on_bridge.append(0)
#         cnt += 1
#         if len(on_bridge) > w:
            
#         if 
#         on_bridge.popleft()
#     else: 
#         on_bridge.append(to_bridge)
#         cnt += 1
        
#     cnt += 1
#     if sum(on_bridge) >= L:
#         cnt += w
#         on_bridge.popleft()
#     else:

# 실패 (다른사람 코드 봣음)

from collections import deque
n,w,L = map(int,input().split())
truck = deque(map(int,input().split()))

bridge = deque([0]*w)
time = 0
while bridge:
    time += 1
    bridge.popleft()
    if bridge and truck:  # 브릿지 없애면 동작함
        if sum(bridge)+ truck[0] <= L:
            bridge.append(truck.popleft())
        else:
            bridge.append(0)
    
print(time)
        
    
    
    