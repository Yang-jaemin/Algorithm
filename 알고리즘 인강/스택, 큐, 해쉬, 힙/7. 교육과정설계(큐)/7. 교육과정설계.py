# y = 'CBA'
# n =3
# tmp = ''
# for i in range(3):
#     c = input()
#     for x in c:
#         if x == 'C':
#             tmp += x
#         elif x == 'B':
#             tmp += x
#         elif x == 'A':
#             tmp += x
#     if tmp == 'CBA':
#         print('#%d Yes' %(i+1) )
#         tmp = ''
#     else:
#         print('#%d No' %(i+1))
#         tmp = ''


# 큐사용
from collections import deque
need = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft(): # 순서대로 해야하니까 pop도 앞에서 부터 , for도 앞에서부터 돌기 때문
                print("#%d NO" %(i+1))
                break
    else: 
        if len(dq) == 0:   # 만약 순서 맞게 pop다 되어서 dq에 남은 게 없다면 YES
            print("#%d Yes" %(i+1))
        else:           # 뭔가가 남아있으면
            print("#%d NO" %(i+1))