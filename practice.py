# 2. k번째 수
T = map(int,input())

for i in range(T):
    n,s,e,k = map(int,input().split())
    a = list(map(int,input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(i+1,a[k-1]))

     