from collections import deque
n,m,v = map(int,input().split())
# 인접행렬생성 -> 인접리스트 질문
check = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    check[a][b] = check[b][a] = 1
# 방문한곳 체크하기 위해서 visted 리스트 
visited = [0]*(n+1)
res = []
# BFS 에서 사용할 큐
Q = deque()

def DFS(L,V): # 처음 탐색 시작하는 것을 넘겨주자 # 끝이 정해진 DFS
        visited[V] = 1
        res.append(V)
        
        if L == n:
            for a in res:
                print(a, end = ' ') 
                
        else:
            for i in range(1,n+1):
                if visited[i] == 0 and check[V][i] == 1:
                
                    DFS(L+1,i)
            
def BFS(V):
    Q.append(V)
    visited[V] = 0  # DFS에서 다 방문이 되어있을거니까 (1로) 이제 BFS에서는 0으로 방문처리를 해주면된다, ㅇㅇ
    
    while Q:
        A = Q.popleft()
        print(A, end = ' ')
        
        for j in range(1,n+1):
            if visited[j] == 1 and check[A][j] == 1:
                Q.append(j)
                visited[j] = 0  
        
DFS(1,v)
print()
BFS(v)