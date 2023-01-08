n = int(input())
card = list(map(int,input().split()))
coin = 0

while len(card) != 1:
    cha = []
    for i in range(1,len(card)):
        cha.append(abs(card[i]- card[i-1]))
    
    for j in range(len(cha)):
        if cha[j] ==  max(cha):
            coin += card[j]+card[j+1]
            if card[j] >= card[j+1]:
                card[j] = card[j]
            else:
                card[j] = card[j+1]
        card.remove(card[j+1])
        break
print(coin)


        
    
    
    
    