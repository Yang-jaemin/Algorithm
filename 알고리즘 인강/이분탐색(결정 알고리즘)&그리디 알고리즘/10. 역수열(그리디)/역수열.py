## 넘무 어렵다 어케생각함 이걸


n = int(input())
a = list(map(int,input().split()))
check = [0]*n

for i in range(n):
    for j in range(n):
        if a[i] == 0 and check[j] == 0:
            check[j] = i+1
            break
        elif check[j] == 0:
            a[i] -= 1
for x in check:
    print(x,end = ' ')