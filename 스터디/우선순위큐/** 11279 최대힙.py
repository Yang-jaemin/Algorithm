import heapq
import sys
n = int(sys.stdin.readline().rstrip())
h = [0]*n # 최소힙으로 작동

for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        print(-heapq.heappop(h))
    else:
        heapq.heappush(h,-a)



import sys
import heapq

n = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(n):
  v = int(sys.stdin.readline().rstrip())
  if v == 0:
    if heap:
      print(-heapq.heappop(heap))
    else:
      print(0)
  else:
    heapq.heappush(heap, -v)
