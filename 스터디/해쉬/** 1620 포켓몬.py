# 시간초과

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
d = {}
for i in range(n):
    a = sys.stdin.readline().rstrip()
    d[a] = i+1

for _ in range(m):
    b = sys.stdin.readline().rstrip()
    if b.isdigit():
        for x,y in d.items():
            if y == int(b):
                print(x)
    else:
        print(d.get(b))


# dict를 두개 만들자
import sys
n, m = map(int, sys.stdin.readline().split())

to_no = {}
to_name = {}

for i in range(n):
  name = sys.stdin.readline().rstrip()
  to_no[name] = i+1
  to_name[i+1] = name
#ans = []
for _ in range(m):
  v = sys.stdin.readline().rstrip()
  if v.isdigit(): #any(c.isdigit() for c in v):
    print(to_name[int(v)])
    #ans.append(to_name[int(v)])
  else:
    print(to_no[v])
    #ans.append(str(to_no[v]))
#print("\n".join(ans))
