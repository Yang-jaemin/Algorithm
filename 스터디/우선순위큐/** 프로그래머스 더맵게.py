#   틀림
import heapq

def solution(scoville, K):
    cnt = 0
    KK = 0
    heapq.heapify(scoville)
    
    while KK < K:
        if not scoville:
            cnt = -1
            break
        else:
            a = heapq.heappop(scoville)
            
            if not scoville:
                cnt = -1
                break
                
            b = heapq.heappop(scoville)
            KK += a+(b*2)
            cnt += 1
        
    return cnt


###########################
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b * 2)
        answer += 1
    return answer