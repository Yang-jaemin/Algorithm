# 딕셔너리 사용
# 왜 딕셔너리가 훨빠르지??
# 딕셔너리로 풀라고 하신 이유??
cnt = 0
n,m = map(int,input().split())
A = set()
s = list(input() for _ in range(n))
for c in s:
        A.insert(c)
e = list(input() for _ in range(m))
for a in e:
    if a in A:
        cnt +=1
print(cnt)

# # 리스트 사용
# n,m = map(int,input().split())
# A = []
# E = []
# cnt = 0
# for _ in range(n):
#     q = input()
#     A.append(q)
# for _ in range(m):
#     p = input()
#     E.append(p)
    
# for c in E:
#     if c in A:
#         cnt +=1
# print(cnt)
