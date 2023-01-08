# 각 배열이 어디를 가리키는지 알려주는 변수 p1,p2가 있어야해
# a1[p1]과 a2[p2]를 비교하면서 순서대로 넣어줘 append
# p1이 들어간다면 +1해주고 p2가 들어간다면 +2 해주고
# while 문을 이용해서 반복이 가능하고 
# while 둘중 하나라도 주어진 최대 인덱스 값을 넘거나 같아지게 된다면 while문 종료하게 만들기
# while 참: 일때만 돈다
p1 = p2 = 0
n = 3
m = 5
a1 = [1,3,5]
a2 = [2,3,6,7,9]
c = []

while p1 < n and p2 < m:
    if a1[p1] <= a2[p2]:
        c.append(a1[p1])
        p1+=1
    else:
        c.append(a2[p2])
        p2+=1
else: 
    if p1 < n:
        c = c + a1[p1:] # 더하면 리스트가 합쳐지면서 들어가고 append하면 리스트 통째로 맨뒤 인덱스에 들어간다.
    else:
        c = c + a2[p2:]
        
print(c)