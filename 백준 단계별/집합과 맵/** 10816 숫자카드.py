# 시간초과
# import sys
# n = int(sys.stdin.readline())
# mycard = list(map(int,sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# yourcard = list(map(int, sys.stdin.readline().split()))
# d = {}

# for a in yourcard:
#     d[a] = mycard.count(a)

# for j in d.values():
#     print(j,end = ' ')
# ------------------------------------------------------

# 다른사람 코드

n = int(input())
arr1 = list(map(int, input().split()))

dict1 = {}
# 숫자카드와 개수를 딕셔너리에 담기
for i in arr1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1


m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if i in dict1:
        print(dict1[i], end=' ')    # 존재하는 숫자 카드라면
    else:
        print(0, end=' ')   
    
