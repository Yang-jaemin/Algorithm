import itertools as it
n , f = map(int,input().split())
b = [1]*n
for i in range(1,n): # 1하고 n은 어떻게 해도 1임
    b[i] = b[i-1]*(n-1)/i # 조합(이항계수)

a = list(range(1,n+1))
    
for tmp in it.permutations(a): # permutations: 순열을 만들어줌 , permutations(a,3) 하면 a중에서 3개만 뽑아서 순열을 만들어라    
    sum = 0
    for L,x in enumerate(tmp):
        sum += (x*b[L])
    if sum == f:
        for x in tmp:
            print(x,end = ' ')
        break