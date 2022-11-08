# 1시간 정도
# 처음에 전체 넓이를 구하고 나머지를 빼는 방식으로 생각했음
# 그리고 젤 높은 넓이가 나오면 다른 if 문이 실행되게 했음
# 

n =  int(input())
a = []
for _ in range(n):
    s,e = map(int,input().split())
    a.append((s,e))
a.sort()
w = (a[n-1][0]+1)-a[0][0] # 기둥면은 길이가 1이니까 +1 ==> 가로길이
a.sort(key = lambda x : (x[1],x[0]))
h = a[n-1][1] # 세로길이
m = a[n-1][0] # 제일 높을때 가로
a.sort(key = lambda x : (x[0],x[1]))
total = w*h  # 전체넓이
x1 = a[0][0]
y1 = a[0][1]
h1 = 0 
w1 = 0
long = 0
for x2,y2 in a:
    if x2 <= m:
       if y2>y1:
        h1 = h-y1
        w1 = x2-x1
        x1 = x2
        y1 = y2
        total -= h1*w1
        print(total)
    if x2 > m:
        if  long <= y2:
            long = y2
total -= (h-long)*(a[n-1][0]-m)
print(total)
        
    
    
    