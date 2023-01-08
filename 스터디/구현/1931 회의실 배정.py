# 그리디
n = int(input())
time = []
cnt = 0
for _ in range(n):
    s,e = map(int,input().split())
    time.append((s,e))
    
time.sort(key = lambda x: (x[1],x[0]))

# [(0, 4), (1, 4), (3, 5)]

# [(4, 0), (4, 1), (5, 3)] # 정렬 기준 값

et = 0
for s,e in time:
    if s>= et:
        cnt +=1
        et = e
print(cnt)



######################

import sys

n = int(input())
meetings = []

for i in range(n):
  s, e = map(int, sys.stdin.readline().split())
  meetings.append((e, s)) # 정렬 편의성을 위해 순서를 바꿔 저장

meetings.sort() # 정렬하면 종료시간이 빠른 순, 종료시간이 같다면 시작시간이 빠른 순으로 정렬된다

cnt = 0
pos = 0
for meeting in meetings:
  if meeting[1] >= pos:
    cnt += 1
    pos = meeting[0]

print(cnt)
