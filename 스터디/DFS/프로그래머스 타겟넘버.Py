numbers = [4, 1, 2, 1]
target = 2
n = len(numbers)
cnt = [0]

def DFS(L,total):
    if L == len(numbers):
        if total == target:
            cnt[0] += 1
            return
    else:
        DFS(L+1,total+numbers[L])
        DFS(L+1,total-numbers[L])
                
DFS(0,0)
print(cnt[0])