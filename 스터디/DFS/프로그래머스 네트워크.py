from collections import deque
def solution(n, computers):
    def DFS(num):
        for k in nA[num]:
            if check[k] == 0:
                check[k] = 1
                DFS(k)
        
    N = len(computers)
    A = [[] for _ in range(N)]
    check = [0]*n
    cnt = 0
    nA = []
    for i in range(N):
        for j in range(len(computers[i])):
            
            if i == j:
                continue
                
            if computers[i][j] == 1:
                A[i].append(j)
                A[j].append(i)
    for x in A:
        x = set(x)
        nA.append(x)
    print(nA)  
    for i in range(n):
        if check[i] == 0:
            check[i] = 1
            DFS(i)
            cnt += 1
    print(cnt)
    
solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])