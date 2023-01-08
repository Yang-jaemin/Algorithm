n = input()
check = set()
for i in range(1,len(n)+1):
    for j in range(len(n)):
        if j+i <= len(n):
            check.add(n[j:j+i])
print(len(check))




s = input()
l = len(s)
x = set()
for i in range(l):
  for j in range(i+1, l+1):
    x.add(s[i:j])
print(len(x))