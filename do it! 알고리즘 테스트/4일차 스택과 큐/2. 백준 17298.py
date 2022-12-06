# 인덱스를 활용해서 스택을 사용할거임
# 혹시 잘 모르겠으면 강의 다시 보자
n = int(input())
A = list(map(int,input().split()))
answer = [0]*n  # 답을 넣을 장소
stack = []      
for i in range(n):
    while stack and A[stack[-1]] < A[i]:  
        answer[stack.pop()] = A[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

result = ''
for i in range(n):
    result += str(answer[i]) + ' '
    
print(result)