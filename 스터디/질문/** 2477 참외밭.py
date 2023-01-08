# 다시 생각해보자
n = int(input())
A = []
h = 0
width = 0
m_h = 0
m_w = 0
kkk = True
for _ in range(6):    
    direct,w = map(int,input().split())
    A.append((direct,w))
    
for i,j in A:
    if i>2:
        if h <= j:
            h = j
    else:
        if width <= j:
            width = j

for k in range(1,5):
    if A[k-1][0] == A[k+1][0]:
        if kkk:
            m_h = A[k+1][1]
            kkk = False
        else:
            m_w = A[k-1][1]
            

total = (h * width) - (m_h * m_w)
print(total*n)
