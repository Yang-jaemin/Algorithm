# 재귀함수 : 자기자신을 호출 (스택을 이용)
# 반복문의 대체제
def DFS(x):
    if x>0:
        print(x)
        DFS(x-1) # 3 2 1

def DFS(x):
    if x>0:
        DFS(x-1)
        print(x, end = ' ') # 1 2 3   왜? 스택이여서

    
if __name__ == "__main__"
    n =int(input())
    DFS(n) # 깊이 우선탐색