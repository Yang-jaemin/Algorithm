# 
def btw(arr):
    global min_num
    cnt_w = 0
    cnt_b = 0
    ccnt = 0
    for p in range(8):
        for q in range(8):
            if W[p][q] != arr[p][q]:
                ccnt+=1
    else:
        cnt_w = ccnt
        ccnt = 0
    
    for o in range(8):
        for s in range(8):
            if B[o][s] != arr[o][s]:
                ccnt+=1
    else:
        cnt_b = ccnt
        ccnt = 0
    if min(cnt_w,cnt_b) < min_num:
        min_num = min(cnt_w,cnt_b)
        AA = []


n,m = map(int,input().split())
A = list()
W = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]
B = [['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]
AA = []
min_num = 100000000
for i in range(n):
    a = list(input())
    A.append(a)

# for y in range(n-7):
#     for x in range(m-7):
#         AA = A[y:y+8][x:x+8]
#         btw(AA)
# print(min_num)

# for s in range(n-7):
#     for d in range(m-7):
#         for x in range(d,d+8):
#             for y in range(s,s+8):
#                 AA.append(A[y][x:x+8])
#             btw(AA)
# print(min_num)

# for i in range(len(A)-8):
#     for j in range(len(A)-8):
#         AA = a([row[j:j+m] for row in a[i:i+n]])
#         print(AA)

    