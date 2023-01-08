n = int(input())
body = []
for i in range(n):
    a, b = map(int,input().split())
    body.append((a,b))
body.sort(reverse = True) # 내림차순

largest = 0 # 최댓값 찾는 과정으로 하면된다.
cnt = 0
s = body[0]
# 키 제일큰애는 무조건 선발 (선발조건 : 둘다 크던가 , 둘중 하나만 크던가)
# 그러면 그 밑에는 몸무게로 이겨야만 선발
for h,w in body:
    if w > largest:
        largest = w
        cnt += 1
        
print(cnt)

    