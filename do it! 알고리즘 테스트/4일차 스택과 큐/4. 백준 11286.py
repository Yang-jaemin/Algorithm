# 우선순위 큐 다시봐야댐
from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
n = int(input())
Q = PriorityQueue() # 우선순위큐
for _ in range(n):
    a = int(input())
    if a == 0:
        if Q.empty():
            print('0\n')
        else:
            temp = Q.get()
            print(str((temp[1]))+'\n')
    else:
        Q.put((abs(a),a)) # 음수 우선 정렬하도록 구성
        