s = [0]*5
A= (1,2,3,1,2)
for i in range(1,5):
    s[i]=s[i-1]+A[i]
print(s)