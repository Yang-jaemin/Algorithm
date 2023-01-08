# https://school.programmers.co.kr/learn/courses/30/lessons/86971
def solution(n, wires):
    answer = 2147000000
    
    for k in range(wires):
        a = wires.pop(k)
        
        A = [[] for i in range(n)]
        check = [0]*(n+1)
        
        for a,b in wires:
            A[a].append(b)
            A[b].append(a)
            
        # 나누어진 트리의 송전탑 개수를 세서 구하기
            
            
            
        
        wires.insert(a,k)
            
    return answer

# 1. 구현
# 2. DFS(Backtracking),BFS
# 5. 해쉬
# 3. 완전탐색

# 4. 그리디
# 스택,큐,힙
# 6. 정렬
# 7. 그래프
# 8. 트리
# 9. DP
# 10.이분탐색