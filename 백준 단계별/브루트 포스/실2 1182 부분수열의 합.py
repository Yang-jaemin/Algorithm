# 브루트포스 2강  # 조합  # 부분집합
# 1182
from itertools import combinations
n,m = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
for i in range(1,len(A)+1):
    a = list(combinations(A,i))
    for answer in a:
        if sum(answer) == m:
            cnt += 1

print(cnt)

# 백트래킹으로도 가능