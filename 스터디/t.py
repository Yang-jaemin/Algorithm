import sys
sys.setrecursionlimit(10**9)

# 루트가 1인데 1,6의 부모를 어떻게 구하지..?
def DFS(start):
    global check
    global d
    global total_d
    
    if start != 1 and len(A[start]) == 1:
        total_d += d
        return
    if check[start] == 1:
        return
    check[start] = 1

    for i in A[start]:
        d = d+1
        DFS(i)
        d = d-1
    
n = int(input())
A = [[] for _ in range(n+1)] # 인접리스트
check = [0]*(n+1)
d = 0
total_d = 0
answer = []
for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)
DFS(1) #

if total_d % 2 == 0:
    print('No')
else:
    print('Yes')
    