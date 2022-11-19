# 구간 합
# 슈도 코드
# n 값 m값 받고
# num에 리스트로 받아주고
# 합 배열 S 변수 선언해주고
# tmp 합배열에 넣어줄 변수 선언

# for x in range(n):
#  tmp에 num[0] 넣고 s[0]에 넣고
#  그대로 tmp에 num[1]더해주고 s[2]에 넣고

# for i in range(M)
#  s,e 구간 입력 받고
#  구간합 출력
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
num = list(map(int,input().split()))
S = [0]
tmp = 0
for i in range(n):
    tmp += num[i]
    S.append(tmp)
for _ in range(m):
    s,e = map(int,input().split())
    print(S[e]-S[s-1])
    