import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 소수인지 판별
def isPrime(i):
    for x in range(2,int(i/2 + 1)):
        if i%x == 0:
            return False
    if i == 1:
        return False
    return True

def DFS(L,num):
    global n
    if L == n:
        print(num)
    else:
        for i in range(1,10):
                if isPrime(num*10 +i):
                    DFS(L+1,num*10 +i)
            
        
    
n = int(input())
DFS(0,0)
