import sys
sys.stdin=open("input.txt", "r")
def DFS(L, s, sum):  # 조합에는 s 가 필요 (스타트 지점)
    global cnt
    if L==k:
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])
 
if __name__=="__main__":
    n, k=map(int, input().split())
    a=list(map(int, input().split()))
    m=int(input())
    cnt=0
    DFS(0, 0, 0)
    print(cnt)