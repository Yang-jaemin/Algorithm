# 투포인터 핵심 , 골드 4
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
cnt = 0
A.sort()
for K in range(N):
    find = A[K]
    i = 0
    j = len(A)-1
    while i < j:
        if A[i]+A[j] == find:
            if i != K and j != K:
                cnt += 1
                break
            elif i == K:
                i +=1
            elif j == K:
                j -= 1
            
        elif A[i]+A[j] > find:
                j -= 1
        else:
                i += 1
            
print(cnt)
        
            
