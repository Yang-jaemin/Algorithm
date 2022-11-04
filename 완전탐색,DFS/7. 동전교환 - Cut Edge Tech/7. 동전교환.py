def DFS(L,sum):
    global res
    if L > res: # res가 최소 레벨인데 현재 최소 레벨보다 L이 더 갈필요가 없다는 뜻 임
        return
    if sum > m:
        return
    if sum == m:
        if L<res: # 여기서 처음에는 지역변수여서 global 안해주면 참조 불가 ㅇㅇ
            res = L
    else:
        for i in range(n):
            DFS(L+1,sum+a[i])


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res = -2147000000  # 최소니까 min
    a.sort(reverse = True)  # sort 해서 최소갯수를 먼저 구하고 나머지는 컽
    DFS(0,0)
    print(res)