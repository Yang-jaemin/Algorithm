# 툴람 - > 맞음
n,m = map(int,input().split())
not_see = []
not_hear = []

for _ in range(n):
    a = input()
    not_hear.append(a)

for _ in range(m):
    b = input()
    not_see.append(b)

not_see = set(not_see)
not_hear = set(not_hear) 
not_seehear = sorted(list(not_see & not_hear))

print(len(not_seehear))

for q in not_seehear:
    print(q)


#a = [2,3,4,1]
#b = sorted(a) # b = [1,2,3,4], a 그대로
#a.sort()

# 쌤 코드
n, m = map(int, input().split())
ans = 0
d = set()
ans = []
for _ in range(n):
  d.add(input())
for _ in range(m):
  v = input()
  if v in d:
    ans.append(v)
ans.sort()
print(len(ans))
for v in ans:
  print(v)
