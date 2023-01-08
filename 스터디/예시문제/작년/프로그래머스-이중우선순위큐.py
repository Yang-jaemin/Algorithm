import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    total = list()
    for c in operations: #1000000
        if c[0] == 'I':
            heapq.heappush(min_heap,int(c[2:]))
            heapq.heappush(max_heap,-(int(c[2:])))
            total.append(int(c[2:]))
                           
        elif c == 'D -1':
            if min_heap:               
                a = heapq.heappop(min_heap) # O(log N)
                max_heap.remove(-a) # O(N)
            if total:
                total.remove(a) # O(N)
            else:
                continue          
        elif c == 'D 1':
            if max_heap:               
                a = heapq.heappop(max_heap)
                min_heap.remove(-a)
            if total:
                total.remove(-a)
            else:
                continue 
    if total:
        answer = [max(total),min(total)]               
    else:
        answer = [0,0]
                           
    return answer

# 1. min/max heap 유지, lazy 하게 삭제하기 --- set() 으로 지금까지 지워진 숫자 관리
# 2. orderedset