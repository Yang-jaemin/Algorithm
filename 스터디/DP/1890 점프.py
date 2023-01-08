n = int(input())
A = [list(map(int, input().split())) for _ in range(n)] # 리스트 저장
dp = [[0] * n for _ in range(n)] # dp 저장
dp[0][0] = 1 # 초기 값

# 반복문을 통해 갈 수 있는 그래프의 좌표를 탐색
for i in range(n):
    for j in range(n):

        # 현재 탐색하는 좌표가 오른쪽 맨 끝 점이면 반복을 멈춘다.
        if i == n - 1 and j == n - 1:
            break

        d = i + A[i][j]
        r = j + A[i][j]
        if d < n:
            dp[d][j]+= dp[i][j]
        
        if r < n:
            dp[r][j] += dp[i][j]
print(dp[n-1][n-1])


# RECURSIVE

import sys

N = int(sys.stdin.readline())
B = []
for _ in range(N):
  B.append(list(map(int, sys.stdin.readline().split())))
M = [[-1] * N for _ in range(N)]

def sol(r, c):
  if r == N-1 and c == N-1:
    return 1
  if r < 0 or r >= N or c < 0 or c >= N:
    return 0
  if M[r][c] != -1:
    return M[r][c]
  dist = B[r][c]
  if dist == 0:
    M[r][c] = 0
  else:
    M[r][c] = sol(r + dist, c) + sol(r, c + dist)
  return M[r][c]

print(sol(0, 0))

# ITERATIVE

import sys

N = int(sys.stdin.readline())
B = []
for _ in range(N):
  B.append(list(map(int, sys.stdin.readline().split())))
M = [[0] * N for _ in range(N)]
M[0][0] = 1

def sol():
  for r in range(N):
    for c in range(N):
      if B[r][c] == 0:
        continue
      nr = r + B[r][c]
      nc = c + B[r][c]
      if nr < N:
        M[nr][c] += M[r][c]
      if nc < N:
        M[r][nc] += M[r][c]
  return M[-1][-1]

print(sol())

