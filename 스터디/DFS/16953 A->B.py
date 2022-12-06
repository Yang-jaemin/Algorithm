# 1트
# IEEE-754 spec floating point
# 0.1+0.1 != 0.2
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
                if m % 2 == 0:
                    cnt += 1
                    DFS(m/2)
                
n,m = map(int,input().split())
cnt = 0
DFS(m)

# 2 -> 162
# 2
# 4 21
# 8 41 42
# 16 81 82 84
# 