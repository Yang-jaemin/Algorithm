# 딕셔너리 활용
n = int(input())
p = dict() # 빈 딕셔너리

for i in range(n):
    word = input() # 단어 하나 받음
    p[word] = 1    # 단어가 key 값이 되는거고  value를 1로 지정해준거임
for i in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items(): # 딕.items() 하면 key 랑 value가 같이 나옴 ㅇㅇ
    if val == 1:
        print(key)
        break