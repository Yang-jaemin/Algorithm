# https://school.programmers.co.kr/learn/courses/30/lessons/142085
# 다른 사람 풀이 봤음 , 힙사용
import heapq
def solution(n, k, enemy):
    heap = []
    answer = 0
    cnt = 0
    if len(enemy) == k:
        cnt = len(enemy)
        return cnt
    for i in range(len(enemy)):
        if n >= enemy[i]:
            heapq.heappush(heap, -enemy[i])
            n -= enemy[i]
            cnt += 1
        else:
            if k > 0: 
                if heap:
                    a = -heapq.heappop(heap)
                    k -= 1
                    cnt += 1
                    if a > enemy[i]:
                        n += a - enemy[i]
                        heapq.heappush(heap, -enemy[i])      
                    elif a == enemy[i]:
                        heapq.heappush(heap, -enemy[i])    
                    else:
                        heapq.heappush(heap, -a)           
                else:
                    cnt += 1
                    k -= 1       
            else:
                break     
    return cnt



###################

# n = 6
# k = 1
# enemy = [2, 1, 4, 3, 7]

# 위엣거
# [4, 3, 3, 2] 넣고, 7 이 들어왔을때
# 최대값인 4를 빼고, 힙은 [3, 3, 2] 가 되고, 7과 4를 비교해서 3가지 경우에 따라 처리

# 아랫거
# [4, 3, 3, 2] 넣고, 7 이 들어왔을때
# 힙에 7을 넣고 [7, 4, 3, 3, 2] 가 되고, 여기서 최대값 7을 빼면 [4,3,3,2] 가 된다


import heapq
def solution(n, k, enemy):
    heap = []
    if len(enemy) == k:
        return len(enemy)
    for i in range(len(enemy)):
        if n >= enemy[i]:
            heapq.heappush(heap, -enemy[i])
            n -= enemy[i]
        else:
            if k > 0: # 무적권 사용 가능
                heapq.heappush(heap, -enemy[i])
                n -= enemy[i]
                largest = -heapq.heappop(heap)
                n += largest
                k -= 1       
            else: # 무적권 없음 - 종료
                return i
    return len(enemy)