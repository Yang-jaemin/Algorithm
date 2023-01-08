n = int(input()) # 하나만 입력 받을때는 int(input())

ch = [0]*(n+1) # n까지 표시되는 인덱스만큼 생성
cnt = 0        # 카운팅 할거임

for i in range(2,n+1): # 2부터 시작, 2는 소수니까 cnt +1
    if ch[i] == 0:
        cnt += 1
        for j in range(i,n+1,i): # range(i,n+1,i) 3번째 인자는 스텝인데 i만큼 증가하는거임
            ch[j] = 1
            
print(cnt)