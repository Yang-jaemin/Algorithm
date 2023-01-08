# https://school.programmers.co.kr/learn/courses/30/lessons/12936
def DFS(L,arr):
    global cnt
    global n
    if L == n:
        cnt += 1
        if cnt == k:
            print(arr)
        
    else:
        for i in range(1,n+1):
            if check[i] == 0:
                check[i] = 1
                arr.append(i)
                DFS(L+1,arr)
                arr.pop()
                check[i] = 0
                
n = int(input())
k = int(input())
check = [0]*(n+1)
cnt = 0
DFS(0,[])

#############

check = [0]*(n+1)
cnt = 0
def DFS(L,arr,n,k):
    if L == n:
        cnt += 1
        if cnt == k:
            return arr
        
    else:
        for i in range(1,n+1):
            if check[i] == 0:
                check[i] = 1
                arr.append(i)
                DFS(L+1,arr,n,k)
                arr.append(i)
                check[i] = 0
                
def solution(n, k):
    global cnt
    answer = DFS(0,[],n,k)
    return answer