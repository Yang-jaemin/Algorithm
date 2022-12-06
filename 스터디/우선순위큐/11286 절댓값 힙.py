import heapq
import sys
n = int(sys.stdin.readline().rstrip())
h = []
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a == 0:
        if not h:
            print(0)
        else:
            b , c = heapq.heappop(h)
            print(c)
    else:
        heapq.heappush(h, (abs(a), a))
# [1,2]
# 