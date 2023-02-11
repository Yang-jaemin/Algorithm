n,k = map(int,input().split())
arr = list(range(1,n+1))
answer = '<'
idx = 0
while arr:
    idx = idx + (k-1)
    if idx >= len(arr):
        idx = idx%len(arr)
        if len(arr) == 1:
            answer += str(arr[idx])
            answer += '>'
        else:
            answer += str(arr[idx])
            answer +=', '
        arr.remove(arr[idx])
    else:
        if len(arr) == 1:
            answer += str(arr[idx])
            answer += '>'
        else:
            answer += str(arr[idx])
            answer += ', '
        arr.remove(arr[idx])
print(answer)