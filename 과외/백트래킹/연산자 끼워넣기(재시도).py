# 슈도코드
#DFS
import sys
sys.setrecursionlimit(10**6)
def DFS(L,res):
    global sum
    if L == N-1:
        for r in range(L):
            if res[r] == '+':
                sum += A[r+1]
            elif res[r] == '-':
                sum -= A[r+1]
            elif res[r] == '*':
                sum *= A[r+1]
            elif res[r] == '%':
                if sum < 0:
                    sum = -((-sum) //A[r+1])
                else:
                    sum = sum // A[r+1]
        else:
            answer.append(sum)
            sum = A[0]
                
        return
    else:
        for y,val in enumerate(S):
            # 방문했으면 건너뛰기
            if check[y]==1:
                continue
            else:
                res.append(val)
                check[y] = 1
                DFS(L+1,res)
                # 백트래킹
                res.pop()
                check[y] = 0
        
    
# N 받기(숫자의 개수)
N = int(input())
# A 수열 받기 (숫자 모음 - 리스트로)
A = list(map(int,input().split()))
#  연산자 숫자 받기
plus,minus,mul,di = map(int,input().split())
# S 숫자 받은거 만큼 문자열로 저장
S = []
for i in range(plus):
    S.append('+')
for i in range(minus):
    S.append('-')
for i in range(mul):
    S.append('*')
for i in range(di):
    S.append('%')
sum = A[0]
check = [0]*len(S)
res = []
answer = []
DFS(0,res)
print(max(answer))
print(min(answer))
    

