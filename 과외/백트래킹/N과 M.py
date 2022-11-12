# 중복 없는 순열 조합
def DFS(L):
    if n == 2:
        for i in range(1,n+1):
            if ch[i] == 1:
                print(i, end = ' ')
                return
    else:
        for i in range(1,n+1):
            if ch[i]== 0:
                ch[i] = 1
                DFS(L+1)
                ch[i] = 0
                DFS(L+1)
            else:
                continue
            
n, m = map(int, input().split())
ch = list(range(n+1))
DFS(0)
