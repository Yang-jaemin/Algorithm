# 딕셔너리 사용
cnt = 0
n,m = map(int,input().split())
A = dict()
s = list(input() for _ in range(n))
for c in s:
        A[c] = 0
e = list(input())
for a in s:
    if a in c:
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
