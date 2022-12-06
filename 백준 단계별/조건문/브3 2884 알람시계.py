s,b = map(int,input().split())
# 일단 다 분으로 바꿔
early_total_b = s*60 + b -45
if early_total_b < 0:
    print(23,60+early_total_b)
else:
    print(early_total_b//60,early_total_b % 60) 

## 다른코드
# 이게 더 좋음
s,b = map(int,input().split())

c = (s*60+b-45)%1440
print(c//60,c%60)