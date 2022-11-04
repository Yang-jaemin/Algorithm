def DFS(l,sum):
    global largest
    if l == n:   # index 번호
        if sum <= c and largest < sum:
            largest = sum
            
    else:  
        DFS(l+1,sum + a[l])
        DFS(l+1,sum)    

if __name__ == '__main__':
    c , n = map(int,input().split())
    a = []
    largest = -2147000000
    for _ in range(n):
        k = int(input())
        a.append(k)
    DFS(0,0)
    print(largest)