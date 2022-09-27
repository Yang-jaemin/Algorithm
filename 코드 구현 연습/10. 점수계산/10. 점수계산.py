n = int(input())
a = list(map(int,input()))

sum = 0
cnt = 0
for x in a:
    if x == 1:
        cnt += 1
        sum = sum+cnt
    else:
        cnt = 0