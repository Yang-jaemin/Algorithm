#from collections import defaultdict
# s =  input().upper()
# s_list = list(set(s))
# cnt = []
# for x in s_list:
#     cnt.append(s.count(x))

# if cnt.count(max(cnt)) >= 2:
#     print("?")
# else:
#     print(s_list[cnt.index(max(cnt))])

s =  input().upper()
va = []
d = {}
cnt = []
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
    
for a in d.values():
    va.append(a)
maxx = max(va)
print(maxx)
if va.count(maxx) >= 2:
    print('?')
else:
    for k , v in d.items():
        if v == maxx:
            print(k)