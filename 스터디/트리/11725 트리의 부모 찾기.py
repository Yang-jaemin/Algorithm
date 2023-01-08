import sys
sys.setrecursionlimit(10**9)

# 루트가 1인데 1,6의 부모를 어떻게 구하지..?
def DFS(start,parent):
    global check

    if start > 1:
        answer.append((start,parent))
    check[start] = 1
    for i in A[start]:
        if check[i] == 0:
            DFS(i,start)
    
        
    
    
n = int(input())
A = [[] for _ in range(n+1)] # 인접리스트
check = [0]*(n+1)
answer = []
for _ in range(n-1):
    a,b = map(int,input().split())
    A[a].append(b)
    A[b].append(a)
DFS(1,0)

#  1
#  |
#  2

#                1
#               / \ 
#              4   6
#             /\    \
#            2  7    3
#                     \
#                      5