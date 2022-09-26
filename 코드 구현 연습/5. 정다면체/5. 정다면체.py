n ,m =  map(int,input().split()) # 정 n 면체 정 m 면체 받아주기

cnt = [0]*(n+m+1)          
# 0으로 초기화된 크기가 n+m+1개인 리스트 만듬 index의 최대가 n+m을 만들기위해서
max = 0 
#최댓값 구하기위해서 

for i in range(1,n+1):  # 각 숫자들을 더해주는 for 문
    for j in range(1,m+1):
        cnt[i+j] = cnt[i+j] + 1
        
for i in range(n+m+1):  # 최대값이 몇인지 가리는 for문 (중복 되어도 상관 x)
    if cnt[i] > max:    # 왜냐면 밑의 포문에서 출력해줄거라서
        max = cnt[i]
        
for i in range(n+m+1):  # 최댓값과 같은 값들을 골라내서 인덱스를 출력
    if cnt[i] == max:
        print(i, end = ' ')

