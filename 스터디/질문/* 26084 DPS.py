#  DFS 직접 구현 - 시간 초과   # 수학적으로 접근 하기
import sys
sys.setrecursionlimit(10**6)
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


############ # 메모리 초과
import itertools
S = list(input())
cnt = 0
S_list = list(itertools.permutations(S,3))  # 순열 1,2 2,1 가능(중복허용), 조합 1,2 1,3  2,3(중복불가)
ww = []
N = int(input())
for _ in range(N):
    word = input()
    ww.append(word[0])

c_word = list(itertools.combinations(ww,3))

for answer in c_word:
    if answer in S_list:
       cnt += 1
print(cnt)

