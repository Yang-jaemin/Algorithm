#from collections import defaultdict
s =  input().upper()
s_list = list(set(s))
cnt = []
for x in s_list:
    cnt.append(s.count(x))

# d = defaultdict(int)
d = {}

for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

for k,v in d:
    ...

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(s_list[cnt.index(max(cnt))])
