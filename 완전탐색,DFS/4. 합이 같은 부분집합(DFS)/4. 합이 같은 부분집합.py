# 상태트리
def DFS(L,sum): # L은 인덱스 번호
    if sum > total//2:
        return
    if L == 6:
        if sum == (total-sum):
            print("yes")
            sys.exit(0)
    else: 
        DFS(L+1,sum+a[L]) # index L을 사용할때
        DFS(L+1,sum)      # index L을 사용안할때
    
    
if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    total = sum(a) # 원소 총합
    DFS(0,0)       # 레벨, sum 넘겨줘야해
    print("NO")