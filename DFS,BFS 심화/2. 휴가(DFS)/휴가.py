# 날짜에 따라서 점프하는 부분집합!!
def DFS(L,s):
    global N,res
    
    if L == N+1: # 7일차에는 상담을 할 수 있기때문에 8일차까지 가야함(N+1)
        if s > res:
            res = s
    else:
        if L + T[L] <= N+1: # 다음상담이 N+1일이 넘어가 버린다면 진행 못함
            DFS(L+T[L],s+P[L]) # 상담한거임
        DFS(L+1,s) # 안한거임
            





N =int(input())
T = [0]*N
P = [0]*N
res = -2147000000
for i in range(N):
    time,pay = map(int,input().split())
    T[i] = time
    P[i] = pay
    # 인덱스를 날짜로 잡고 싶어서 앞에 insert 해줄거임
T.insert(0,0)
P.insert(0,0) # 하나씩 밀림
DFS(1,0) # 시작 날짜, 페이의 합
print(res)