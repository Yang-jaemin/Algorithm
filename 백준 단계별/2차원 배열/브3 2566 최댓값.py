A = []
largest = 0
for i in range(9):
    a = list(map(int,input().split()))
    if max(a)>largest:
        largest = max(a)
    A.append(a)
print(largest)
for i in range(9):
    for j in range(9):
        if A[i][j] == largest:
            print(i+1,j+1)
            break

# 다른 코드

res,x,y=-1,0,0
for i in range(9):
    lis=list(map(int, input().split()))
    for j in range(9):
        if res<lis[j]:
            res,x,y=lis[j],i+1,j+1
print(res)
print(x,y)