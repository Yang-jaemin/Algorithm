def DFS(x):
    if x==0:
        return # 리턴만 쓰면 함수 종료
    else:
        
        DFS(x//2)            # 11//2 = 5 -> 5를 다시 함수에 넣기   2로 계속 나누어서 몫이 0일때까지 하면 2진수임(거꾸로)
        print(x%2,end = ' ') # 11 % 2 = 1 # 거꾸로 해야해서 호출 밑으로 한다.



if __name__ == "__main__":  # 나중에 좀더 알아보자
    n = int(input())
    DFS(n)