# 거리구하는 거니까 BFS
from collections import deque
n = int(input())
A = [[] for _ in range(n+1)]


for _ in range(n):
    Data = list(map(int,input().split()))
    index = 0
    S = Data[index]
    index += 1