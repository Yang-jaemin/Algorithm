A = [[0]*101 for _ in range(101)]
n = int(input())
answer = 0
for i in range(n):
    x,y = map(int,input().split())
    for j in range(y,y+10):
        for k in range(x,x+10):
                A[j][k] = 1
            
for i in A:
    answer += sum(i)
print(answer)

# 다른사람 코드
 
N=int(input())
M=[[0 for _ in range(101)]for _ in range(101)]
for i in range(N):
    a,b=map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            M[i][j]=1
ans=0            
for i in M:
    ans+=i.count(1)
print(ans)           
    