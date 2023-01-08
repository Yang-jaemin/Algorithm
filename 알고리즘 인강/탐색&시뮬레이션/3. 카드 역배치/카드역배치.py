card = list(range(21))#[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
arr = []

for _ in range(10): # _로 변수를 설정하면 변수의 넣는 시간도 줄일수 있음 (그냥 반복)
    n,m = map(int,input().split())
    for i in range((m-n+1)//2):  # 숫자 교환
        card[n+i], card[m-i] = card[m-i], card[n+i] # 스왑

card.pop(0) # 0번 인덱스 뺌
for x in card:
    print(x,end=' ')

    
