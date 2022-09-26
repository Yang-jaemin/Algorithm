n ,k = map(int,input().split()) 
# 2개를 입력받으니까 변수 2개 , 띄어쓰기로 구분해주어야 하니까 input().split()
# input으로 받으면 스트링이니까 map 함수를 통해서 int로 바꿔준다
cnt = 0
# 약수 발견할 때마다 1올라감
for i in range(1,n+1):  # range(n+1)을 해버리면 0부터니까 zero division 발생
    if n % i == 0:      # 약수
        cnt = cnt + 1   # 발견할때마다 1을 더해줘서 순서를 만들어준다 (1번째 2번째)
    if cnt == k:        # k번째가 되면 그 약수(i) 출력
        print(i)
        break
else:                   # for else문 : for문에서 break를 만나지 않으면 실행이 안된다!
    print(-1)