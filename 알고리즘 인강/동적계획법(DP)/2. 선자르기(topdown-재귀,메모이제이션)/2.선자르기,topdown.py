def DFS(num):
    if dy[num] >0:  # 가지치기
        return dy[num] # 만약 dy값이 저장되어있다면 그냥 리턴
    if num == 1:
        return dy[1]
    elif num == 2: # 1과 2는 직관적으로 알수 있다. 그래서 dy[1],dy[2]를 알수 있다.
        return dy[2]
    else:
        dy[num] = DFS(num-1)+DFS(num-2)
        return dy[num]  # DFS(num)의 리턴값이 있어야하니까 리턴을 해줘야한다.
    
        


n = int(input())
dy =  [0]*(n+1) # 메모이제이션을 위해서, 컷엣지
dy[1] = 1
dy[2] = 2
print(DFS(n))
