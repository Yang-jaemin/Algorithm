from itertools import combinations
number = list("1231234")
nnum = linumber)
answer = []
k = 3
n = list(range(len(number)))
tmp = list(combinations(n,k))
for i in tmp:
    cnt = 0
    for j in i:
        number.remove(number[j-cnt])
        cnt+=1
    answer.append(''.join(number))
    number = nnum
print(max(answer))