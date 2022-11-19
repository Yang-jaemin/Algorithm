# 슈도코드 (이건 무작위 배열일때 사용하는거임 그리고 두개만 더하는 거자나 ㅇㅇㅇ  두개만!!!)
# N 입력 받고
N = int(input())
# M 입력 받고
M = int(input())
# N개의 숫자 받고
A = list(map(int,input().split()))

# A.sort()
# i = 0
# j = N-1
# cnt = 0
# while i<j:
#     if A[i]+A[j] > M:
#         j -=1
#     elif A[i]+A[j] < M:
#         i += 1
#     else:
#         cnt += 1
#         i +=1
#         j -= 1
# print(cnt)


# 혹시 DFS 로도 가능 할까?? -> 가능 ㅇㅇ
check = [0]*len(A)
res = [0]*2
cnt = 0
def DFS(L):
    global cnt
    if L == 2:
        if sum(res) == M:
            
            cnt +=1
    else:
        for i in range(len(A)):
            if check[i] == 0:
                check[i] = 1
                res[L] = i
                DFS(L+1)
                check[i] = 0
            else: 
                continue
DFS(0)
print(cnt)
                
                
        