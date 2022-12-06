import heapq
K = 7
scoville = [1, 2, 3, 9, 10, 12]
cnt = 0
KK = 0
heapq.heapify(scoville)
    
while KK < K:
    a = heapq.heappop(scoville)
    b = heapq.heappop(scoville)
    print(a,b)
        
print(cnt)