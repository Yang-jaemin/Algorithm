def DFS(i,arr):
    global N,plus,minus,gop,na,max_value,min_value
    if i == N:
        max_value = max(max_value,arr)
        min_value = min(min_value,arr)
    else:
        if plus > 0:
            plus -= 1
            DFS(i+1,arr + a[i])
            plus += 1
        if minus > 0:
            minus -= 1
            DFS(i+1,arr - a[i])
            minus += 1
        if gop > 0:
            gop -= 1
            DFS(i+1,arr * a[i])
            gop += 1
        if na > 0:
            na -= 1
            DFS(i+1,int(arr // a[i]))
            na += 1
    
        
N =int(input())
a = list(map(int,input().split()))
plus,minus,gop,na = map(int,input().split())

max_value = -1e9
min_value = 1e9
DFS(1,a[0])
print(max_value)
print(min_value)