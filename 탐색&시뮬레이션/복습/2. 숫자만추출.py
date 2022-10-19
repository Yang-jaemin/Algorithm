# isdigit 사용해서 숫자이면 True , 아니면 False
s ='0q2rf4dfkajfj'
a = ''
cnt = 0
for x in s:
    if x.isdigit():
        a+= x
for i in range(1,int(a)+1):
    if int(a) % i == 0:
        cnt += 1
print(cnt)