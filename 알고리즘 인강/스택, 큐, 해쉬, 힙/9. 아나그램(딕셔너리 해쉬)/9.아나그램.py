a = input()
b = input()
str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x,0) + 1 # dict.get(x,0) # 그 값이 존재하면 그 값이 나오고 없으면 0을 누적
for y in b:
    str2[y] = str2.get(y,0) + 1
    
for i in str1.keys(): # str1 의 key들을 다 i에 갖다 박음
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("no")
            break
    else:
        print("no")
        break
else:
    print("yes")

# 수정코드
a = input()
b = input()
sH = dict()

for x in a:
    sH[x] = sH.get(x,0) + 1 # dict.get(x,0) # 그 값이 존재하면 그 값이 나오고 없으면 0을 누적
for y in b:
    sH[y] = sH.get(y,0) -1
    
for x in a:
    if sH.get(x)>0:
        print("no")
        break
else:
    print("yes")