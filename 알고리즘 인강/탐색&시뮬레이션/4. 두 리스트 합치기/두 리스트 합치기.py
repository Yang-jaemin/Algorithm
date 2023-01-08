n = 8
a = [1,3,4,5,6,7,8,9]
m = 5
b = [2,3,6,7,9]
p1 = p2 = 0
c = []

while p1 < n and p2 < m: # while 이니까 and
    if a[p1] <= b[p2]: 
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:     # a가 남는 경우
    c = c + a[p1:]
elif p2 < m:    # b가 남는 경우
    c =  c+ b[p2:]

print(c)