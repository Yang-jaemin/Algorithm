from collections import deque
N,L = map(int,input().split()) # 12 , 3
A = list(map(int,input().split()))
Q = deque()

for i in range(N):
    while Q and Q[-1][0] > A[i]: # 맨 마지막 값이 새로 들어올 값보다 크면
        Q.pop()
    Q.apppend((A[i],i))
    if Q[0][1] <= i-L:
        Q.popleft()
    print(Q[0][0],end = ' ')