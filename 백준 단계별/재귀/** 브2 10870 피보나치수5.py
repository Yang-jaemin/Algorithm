# 메모리 초과

import sys
sys.setrecursionlimit(10**6)

def recur(L,num,ex_num):
    global n
    if L == n:
        print(num)
        return
    else:
        num = ex_num + num
        ex_num = num - ex_num
        recur(L+1,num,ex_num)
        


n = int(input())
recur(1,1,0)