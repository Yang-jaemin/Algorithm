# 이거 왜 무한루프?
from collections import deque

def DFS(V): # 처음 탐색 시작하는 것을 넘겨주자 # 끝이 정해진 DFS
        v[V] = 1
        print(V, end = ' ') # 첫 탐색 숫자 출력해주고
    
        for 
                DFS(i)
# def BFS(k):
#     Q.append(k)
#     v[k] = 0
#     while Q:
#         qq = Q.popleft()
#         print(qq,end = ' ')
#         for i in A[qq]:
#             if v[i] == 1:
#                 Q.append(i)
#                 v[i] == 0
#     return
        
    
n,m,k = map(int,input().split())

A = [[]for _ in range(n+1)]
v =[0]*(n+1)
Q = deque()
answer = []
for i in range(n+1):
    A[i].sort

for _ in range(m): # 인접리스트
    s,e = map(int,input().split())
    A[e].append(s)
    A[s].append(e)

DFS(k)

