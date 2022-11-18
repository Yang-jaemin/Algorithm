# 14888번 문자열 조합으로 풀어보기
#DFS
import sys
sys.setrecursionlimit(10**6)
def DFS(L,res):
    global sum  
    if L == N-1:
        for r in range(L):   # res(조합된 문자 리스트)의 인덱스를 확인해서 순서대로 연산 실행
            if res[r] == '+':
                sum += A[r+1]
            elif res[r] == '-':
                sum -= A[r+1]
            elif res[r] == '*':
                sum *= A[r+1]
            elif res[r] == '%':
                if sum < 0:
                    sum = -((-sum) //A[r+1])   # 음수일 경우 처리
                else:
                    sum = sum // A[r+1]
        else:
            answer.append(sum)   # 계산결과를 answer에 넣어준다
            sum = A[0]           # 초기화(다음 넘어오는 res를 계산해야하니까)
                
        return
    else:
        for y,val in enumerate(S):  # 인덱스와 그 인덱스에 해당하는 연산자를 같이 받고
            # 방문했으면 건너뛰기
            if check[y]==1:
                continue
            else:
                res.append(val)     # 연산자는 res에 집어 넣고
                check[y] = 1        # 사용한 연산자는 check
                DFS(L+1,res)        # 쭉 DFS 내려가기
                res.pop()           # 완료되면 백트래킹
                check[y] = 0
        
    
# 1. N 받기(숫자의 개수)
N = int(input())
# 2. A 수열 받기 (숫자 모음 - 리스트로)
A = list(map(int,input().split()))
# 3. 연산자 숫자 받기
plus,minus,mul,di = map(int,input().split())
# 4. S 숫자 받은거 만큼 문자열로 저장
S = []
for i in range(plus):
    S.append('+')
for i in range(minus):
    S.append('-')
for i in range(mul):
    S.append('*')
for i in range(di):
    S.append('%')

sum = A[0] # DFS에서 계산할때 sum을 사용
check = [0]*len(S) # S의 인덱스를 체크해서 사용했으면 check의 같은 인덱스에 1을 넣을 예정 
res = []           # 문자 리스트의 조합을 넣어줄 리스트
answer = []        # 실제 계산한 값들을 넣어줄 리스트
DFS(0,res)         # level 0 부터 빈리스트를 넘겨줌
print(max(answer))
print(min(answer))
    

