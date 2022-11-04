# 체크리스트 필요 # 복습 요망
def DFS(L):
    if L == m:
        for j in range(L):
            print(res[j],end = ' ')
        print()
        cnt +=1
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i] = 0





n,m = map(int,input().split())
res = [0]*m                     # 뽑은거 출력해야되니까, 만약 2라면 0, 1 만
ch = [0]*(n+1)                  # 체크리스트 
cnt = 0                         # 갯수
DFS(0)