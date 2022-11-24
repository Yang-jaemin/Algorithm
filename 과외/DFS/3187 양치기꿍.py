# DFS로 하는거임
# 블로그 찾아봤음 ㅜㅜ
import sys
sys.setrecursionlimit(10**6)

def DFS(Y,X):
    if Y <= -1 or Y >= n or X <= -1 or Y >= m:
        return False
    if board[Y][X] != '#':
        survive.append(board[Y][X])
        board[Y][X] = '#'
        
        DFS(Y+1,X)
        DFS(Y-1,X)
        DFS(Y,X+1)
        DFS(Y,X+1)
        
n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
survive = [] # 누가 살아남았는지 비교하기 위한 리스트
sur_v = []
sur_k = []

for i in range(n):
    for j in range(m):
        if board[i][j] != '#':
            DFS(i,j)
            if survive.conunt('v') < survive.count('k'):
                sur_k.append(survive.conunt('k'))
            else:
                sur_v.append(survive.conunt('v'))
            
            survive = []
            
print(sum(sur_k),sum(sur_v))