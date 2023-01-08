n = int(input())
fact = 1
cnt = 0
if n == 0:  # n이 0일때도 봐야해
    print(0)
for i in range(n):
    fact = fact*(n-i)
fact =str(fact)

for i in range(1,n+1):
    if fact[-i] == '0':
        cnt += 1
    else:
        print(cnt)
        break