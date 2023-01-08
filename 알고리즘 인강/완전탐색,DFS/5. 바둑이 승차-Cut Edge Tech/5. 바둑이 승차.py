def DFS(l,sum,tsum):
    global largest
    if sum + (total-tsum) < largest:  #시간 줄이기 # 잘모르게쓰무ㅜ
        return
    if l == n:   # index 번호
        if sum <= c and largest < sum:
            largest = sum
            
    else:  
        DFS(l+1,sum + a[l],tsum + a[l])
        DFS(l+1,sum,tsum + a[l])    

if __name__ == '__main__':
    c , n = map(int,input().split())
    a = []
    
    largest = -2147000000
    for _ in range(n):
        k = int(input())
        a.append(k)
    total = sum(a)
    DFS(0,0,0)
    print(largest)