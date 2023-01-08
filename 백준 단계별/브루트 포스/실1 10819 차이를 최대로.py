# 브루트포스 10819 # 순열
# 무식하게 모든 가능한 경우를 전부 시뮬
# 모든 permutaion에 대해서 차이의 합을 구해보자 # python에 permutation 내장함수 사용
from itertools import permutations 
n = int(input()) 
a =  list(map(int,input().split()))

ans = -1 
for p in list(permutations(a)): # p에 순열 하나하나 가 튜플로 들어감 ,, 뒤에 숫자를 안적으면 그냥 가능한 순열 다 내보냄
    sum = 0
    for i in range(n-1):
        sum += abs(p[i]-p[i+1])
    
    if ans < sum:
        ans = sum
print(ans)

# 백트레깅으로도 가능 -> 순열 하나하나 다구해야함