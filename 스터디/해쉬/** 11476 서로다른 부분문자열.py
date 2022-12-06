a = input()
s = 0
e = 0
result = set()
for i in range(1,len(a)+1):
    s = 0 
    e = 0
    for  _ in range(len(a)):
        if e+i <= len(a):
            result.add(a[s:e+i])
        s += 1
        e += 1
print(len(result))

# 부분문자열
s = input()
l = len(s)
x = set()
for i in range(l): # [0 ~ l-1]
  for j in range(i+1, l+1): # [i+1 ~ l]
    x.add(s[i:j])
print(len(x))

     0 1 2
a = [1,2,3]
range(3) => [0,1,2]

range(i, j) => [i ~ j-1]
s[i:j] => [i ~ j-1]
"abcd"
i = 0
   j = 1 a
   j = 2 ab
   j = 3 abc
   j = 4 abcd
i = 1
   j = 2 b
   j = 3 bc
   j = 4 bcd