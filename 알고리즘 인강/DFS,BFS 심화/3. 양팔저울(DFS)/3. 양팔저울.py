def DFS(L,sum):
    global res
    global n
    if L == n:
        if sum > 0 and sum <= s:
            res.add(sum)
    else:
        # 상태트리
        DFS(L+1,sum+chu[L]) # 저울 오른쪽에
        DFS(L+1,sum-chu[L]) # 저울 왼쪽(물통과 같이)
        DFS(L+1,sum)        # 그냥 안씀 
        
n = int(input())
chu = list(map(int,input().split()))
s = sum(chu)
res = set()  # 중복이 있을수 있으니까
DFS(0,0)
print(s-len(res))