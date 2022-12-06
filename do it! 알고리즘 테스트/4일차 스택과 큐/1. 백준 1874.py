# 스택
n = int(input()) # 몇개의 수열
A = [0]*n 
for i in range(n):
    A[i] = int(input())  # 우리가 만들어볼 수열
    
s = []   # 스택
num = 1  # 현재 수열값 (stack에 오름차순으로 넣으니까 1부터 시작인거지 ㅇㅇ)
result = True  # true일때만 스택을 출력
answer = []    # +,- 넣을 문자


##### 핵심
for i in range(n): # A[i] 로 탐색
    su = A[i]      # 현재 만들어야할 수
    if su >= num:  # 만들어야하는 수가 더 크면 
        while su >= num:  
            s.append(num)  # 나올때까지 append
            num += 1       # 오름차순으로 넣어야되니까
            answer.append('+')
        s.pop()            # 만들어야하는 수까지 다 넣었으면 빼야지
        answer.append('-')
    else: # su < num       # 근데 만약 만들어야하는 수보다 num이 작아
        q = s.pop()        # stack 맨 위에껄 보고
        if q > su:         # 만약 스택 맨위에꺼가 만들어야되는 수보다 크면 맨위에꺼는 순서도 아닌데 빼야하니까
            print('no')    # 불가능
            result = False
            break
        else:
            answer.append('-') # 만약 만들어야하는 수가 맨위에 있거나 (q == su)바로 pop 이고  맨위보다 작으면(q < su) 다음수 append하면대          
if result:
    for r in answer:
        print(r)
            
        