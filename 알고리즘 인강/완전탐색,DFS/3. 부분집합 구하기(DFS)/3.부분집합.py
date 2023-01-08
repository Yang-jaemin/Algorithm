# 상태트리 : 그림그려가면서
def DFS(v):
    if v == n+1:
        for i in range(1,n+1):
            if ch[i] == 1:
                print(i,end = ' ')
        print() # 줄바꿈
    else:
        ch[v] = 1 # 사용한다
        DFS(v+1)
        ch[v] = 0 # 사용안한다
        DFS(v+1)

if __name__=='__main__':
    n = int(input())
    ch = [0]*(n+1) # 사용했냐 안했냐를 알수 이쓴 체크 변수가 필요
    DFS(1)