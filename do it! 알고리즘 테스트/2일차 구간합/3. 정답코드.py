import sys
input = sys.stdin.readline
# n 입력받기(수 개수)
# m 입력받기(나누어떨어져야 하는 수)
n,m = map(int,input().split())
# A 입력받기 (원본수열)
A = list(map(int,input().split()))
# S 선언(합배열)
S = [0]*n
# C 선언하기(같은 나머지를 카운트하는 인덱스)
C = [0]*m # 나머지는 아무리 커도 m-1(인덱스가 나머지로 올거임)
# answer 선언하기
answer = 0
S[0] =A[0]
# 합배열 만들기
for i in range(1,n):
  S[i] = S[i-1] +A[i]
# 
# 나눈 값을 인덱스로 하는 C에 1씩 저장
for j in range(n):
    reminder = S[j]%m
    if reminder == 0:
        answer +=1
    C[reminder] +=1

#   만약 C가 1이 넘는다면 나머지가 같은게 2개 이상인거니끼 조합으로 풀기(5개면 5개중 2개 5 C 2 )
for k in range(m):
   if C[k] > 1:
       answer += (C[k]*(C[k]-1) //2)
print(answer)