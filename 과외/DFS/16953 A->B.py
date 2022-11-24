# 1트
def DFS(m):
    global cnt,n
    if int(m+0.5) != int(m) or m < n:
        print(-1)
    else:
        m = int(m)
        if m == n:
            print(cnt+1)
        else:
            if m % 10 == 1:
                m = str(m)
                m = m[:-1]
                m = int(m)
                cnt +=1
                DFS(m)
            else:
                cnt +=1
                DFS(m/2)
                
n,m = map(int,input().split())
cnt = 0
DFS(m)