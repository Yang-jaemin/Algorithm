# 트리가 n가닥으로
def DFS(l):
    if l == m :
        for j in res:
            print(j , end = ' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            res[l] = i
            DFS(l+1)
    
    
    
    
if __name__ == '__main__':
    n, m = map(int,input().split())
    res = [0]*m
    cnt = 0
    DFS(0)
    
