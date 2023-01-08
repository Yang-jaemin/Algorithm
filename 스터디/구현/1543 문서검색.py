answer = input()
a = input()
i = 0
cnt = 0
check = [0]*len(a) # 없애보자

while i+len(a) <= len(answer): # i가 비교하는 시작점, i+len(a)가 비교하는 가장 마지막점이다 근데 그게 answer의 범위를 넘어가면 안되니까
    for j in range(len(a)):    # i+0,i+1,i+2 비교 
        if answer[i+j] == a[j]:
            check[j] = 1       # 전부 맞는지는 check활용
    if sum(check) == len(a):   # 만약 맞다면?
        cnt += 1               # cnt += 1 하고
        i += len(a)            # 겹치면 안되니까 비교한 다음부터 비교
    else:
        i += 1                 # 틀리다면 다음꺼부터 다시비교
    check = [0]*len(a)         # 한번 비교하고는 check 초기화
print(cnt)



answer = input()
a = input()
i = 0
cnt = 0

while i+len(a) <= len(answer): # i가 비교하는 시작점, i+len(a)가 비교하는 가장 마지막점이다 근데 그게 answer의 범위를 넘어가면 안되니까
    flag = True
    for j in range(len(a)):    # i+0,i+1,i+2 비교 
        if answer[i+j] != a[j]:
            flag = False
            break
    if flag:   # 만약 맞다면?
        cnt += 1               # cnt += 1 하고
        i += len(a)            # 겹치면 안되니까 비교한 다음부터 비교
    else:
        i += 1                 # 틀리다면 다음꺼부터 다시비교
print(cnt)