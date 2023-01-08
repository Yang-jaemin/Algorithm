def DFS(L,p):
    global cnt
    if L == n:
        cnt += 1
        for j in range(p):
            print(chr(res[j]+64),end = '') # chr 아스키 문자로 바꿔줌 65가 A
        print()
    else:
        for i in range(1,27): # 26개의 가닥을 뻗을 거니까
            if code[L] == i:  # 1개씩 볼때
                res[p] = i
                DFS(L+1,p+1)
            elif i >= 10 and code[L] == i//10 and code[L+1] == i%10:
                res[p] = i
                DFS(L+2,p+1)



code = list(map(int,input()))
n = len(code) # 종착점
code.insert(n,-1) # 11줄에서 한자리 남았어도 code[L+1] == i%10에서 에러가 안나게
res = [0]*(n+1)
cnt = 0 # 갯수 세야하니까
DFS(0,0) # L, p -> p는 res에 넣을 인덱스 지정
print(cnt)