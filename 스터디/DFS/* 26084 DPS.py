def DFS(L,s,arr):
    global cnt
    global S
    if L == 3:
        if arr in S_list:
            cnt += 1
    else:
        for c in range(s,len(N)):
            if check[c] == 0:
                check[c] = 1
                DFS(L+1,c+1,arr+N[c])
                check[c] = 0
                

def S_DFS(L,arr):
    if L == 3:
        S_list.add(arr)
    else:    
        for i in range(3):
            if S_check[i] == 0: 
                S_check[i] = 1
                S_DFS(L+1,arr+S[i])
                S_check[i] = 0

S =  list(input())
S_check = [0]*3
S_list = set()
for q in range(3):
    S_check[q] = 1
    S_DFS(1,S[q])
    S_check[q] = 0
n = int(input())
N = []
arr = ''
cnt = 0
check = [0]*n
cnt = 0
for _ in range(n):
    a = input()
    N.append(a[0])

for i in range(n):
    check[i] = 1
    DFS(1,0,N[i])
print(cnt)