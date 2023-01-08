# 네임에러
n = input()
start = str(int(n)-len(n)*9) # 189
answer = 0
while answer != int(n):
    answer = int(start)
    for i in range(len(start)):
        answer += int(start[i])
    if answer != int(n):
        start = str(int(start)+1)
    else:
        print(start)

