# 1시간 정도
# 처음에 전체 넓이를 구하고 나머지를 빼는 방식으로 생각했음
# 그리고 젤 높은 넓이가 나오면 다른 if 문이 실행되게 했음
# 예제 입력은 통과를 하는데 다른 케이스가 통과가 안되는듯

n =  int(input())
a = []
for _ in range(n):
    s,e = map(int,input().split())
    a.append((s,e))
a.sort()
w = (a[n-1][0]+1)-a[0][0] # 기둥면은 길이가 1이니까 +1 ==> 가로길이
a.sort(key = lambda x : (x[1],x[0]))
h = a[n-1][1] # 제일 높을때 y좌표
m = a[n-1][0] # 제일 높을때 x좌표
a.sort(key = lambda x : (x[0],x[1]))
total = w*h  # 전체넓이
x1 = a[0][0] # 처음 for문에 들어갈 막대 x좌표
y1 = a[0][1] # 처음 for문에 들어갈 y좌표
h1 = 0       # 빼줄 사각형의 높이
w1 = 0       # 빼줄 사각형의 가로
long = 0
for x2,y2 in a:
    if x2 <= m: # 가장 높은 막대의 왼편
       if y2>y1:
        h1 = h-y1
        w1 = x2-x1
        x1 = x2
        y1 = y2
        total -= h1*w1
    if x2 > m:  # 가장 높은 막대의 오른편
        if  long <= y2:
            long = y2
total -= (h-long)*(a[n-1][0]-m) # 막대 오른쪽의 빼줄 공간 계산
print(total)
        
    
    
    