# 이거 왜 무한루프?
from collections import deque

# def DFS(L,num):
#     if L == 4:
#         for q in answer:
#             print(q,end = ' ')
#             return
#     else:
#         v[num] = 1
#         answer.append(num)
#         for i in A[num]:
#             if v[i] == 0:
#                 DFS(L+1,i) 

def DFS(num):
    print(num,end = ' ')
    v[num] = 1
    for i in A[num]:
        if v[i] == 0:
            DFS(i)
        
def BFS(num):
    Q.append(num)
    v[num] = 0
    while Q:
        qq = Q.popleft()
        print(qq,end = ' ')
        for i in A[qq]:
            if v[i] == 1:
                v[i] == 0
                Q.append(i)
        
    
n,m,k = map(int,input().split())

A = [[]for _ in range(n+1)]
v =[0]*(n+1)
Q = deque()

for _ in range(m): # 인접리스트
    s,e = map(int,input().split())
    A[e].append(s)
    A[s].append(e)
    
for i in range(1,n+1):
    A[i].sort()    

DFS(k)
print()
BFS(k)