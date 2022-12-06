s,b = map(int,input().split())
cook = int(input())
# 시간 -> 2884번이랑 같음
t = (s*60+b+cook)%1440
print(t//60,t%60)