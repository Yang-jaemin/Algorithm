l = int(input())
box = []
for _ in range(l):
    tmp = int(input())
    box.append(tmp)
    
m = int(input('높이 조정 횟수:'))

box.sort()
for _ in range(m):
    box[0]+= 1
    box[l-1] += -1
    box.sort()

print(box[l-1]-box[0])

    