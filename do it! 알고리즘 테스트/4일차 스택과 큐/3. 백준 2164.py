from collections import deque
n = int(input())
A = list(range(1,n+1))
A = deque(A)

while len(A) != 1:
    A.popleft()
    A.append(A.popleft())

print(A[0])