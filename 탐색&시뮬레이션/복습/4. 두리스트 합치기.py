p1 = p2 = 0
n = 3
m = 5
a1 = [1,3,5]
a2 = [2,3,6,7,9]
c = []

while p1 < n and p2 < m:
    if a1[p1] <= a2[p2]:
        c.append(a1[p1])
        p1+=1
    else:
        c.append(a2[p2])
        p2+=1
else: 
    if p1 < n:
        c = c + a1[p1:] 
    else:
        c = c + a2[p2:]
        
print(c)