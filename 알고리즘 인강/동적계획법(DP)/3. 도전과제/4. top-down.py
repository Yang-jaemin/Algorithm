def DFS(num):
    if num == 1:
        return dy[1]
    elif num == 2:
        return dy[2]
    else:
        dy[num] = DFS(num-1) + DFS(num-2)
        return dy[num]
    


n = int(input())
dy = [0] * (n+1)
dy[1] = 1
dy[2] = 2
print(DFS(n))


# D(7) = D(6)+D(5)
# D(6) = D(5)+D(4)
# D(4) = D(4)+D(3)
# D(3) = D(2)+D(1)


