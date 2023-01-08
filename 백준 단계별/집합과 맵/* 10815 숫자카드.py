# 시간초과
# n = int(input())
# mycard = list(map(int,input().split()))
# m = int(input())
# yourcard = list(map(int,input().split()))
# check = [0]* len(yourcard)

# for i in range(len(yourcard)):
#     if yourcard[i] in mycard:
#         check[i] = 1

# for j in check:
#     print(j, end = ' ')
# ----------------------------------------------------------
# 이것도 시간초과

# import sys
# n = int(sys.stdin.readline())
# mycard = list(map(int,sys.stdin.readline().split()))
# m = int(input())
# yourcard = list(map(int,sys.stdin.readline().split()))

# for i in yourcard:
#     if i in mycard:
#         print(1,end = ' ')
#     else:
#         print(0, end = ' ')

# ---------------------------------------------------------
# 딕셔너리 이용
import sys
n = int(sys.stdin.readline())
mycard = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
yourcard = list(map(int, sys.stdin.readline().split()))

d = {}
for i in range(len(mycard)):
    d[mycard[i]] = 0
    
for j in range(m):
    if yourcard[j] in d:  # 찾는게 훨씬 빠르다
        print(1,end = ' ')
    else:
        print(0,end = ' ')
        
# 다른 사람 코드
def test():
    input()
    b = set(input().split()) #내가 가진 값
    input()
    d = list(input().split())    #찾아야 하는 값
    res = ''
    for i in d:
        if i in b:
            res += '1 '
        else:
            res += '0 '
    print(res)

test()
    
    