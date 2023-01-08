# last in first out 나중에 들어간게 먼저나온다 # 구덩이 구조
# 파이썬에서는 따로 스택이라는게 없고 리스트에서 append, pop으로 스택을 구현가능하다 둘다 뒤로 빼고 뒤로 넣으니까 ㅇㅇ
num, m = map(int,input().split())
num =list(map(int,str(num))) # 숫자를 문자열로 바꿔서 하나씩 리스트에 저장, 그냥 하면 안되고 꼭 str로 바꿔야 한다.
stack = []
for x in num:
    while stack and m>0 and stack[-1] <x: # stack이 비어있으면 거짓이 된다. 기억하기 , 마지막으로 들어간 숫자 stack[-1]가 보다 작으면 제거
        stack.pop() # 작아서 제거
        m-=1 # 하나 제거 했으니까 기회 한개썼으니까 m 감소
    stack.append(x) # 자기 보다 작은거 다지웠으니까 자기가 들어가야함
    
if m!= 0: # for 문으로 다 돌았는데 m이 남아서 지워야 할때
    stack = stack[:-m] # 뒤에 날림
    
res = ''.join(map(str,stack)) # 스택 안에 있는 문자인 숫자를 다 더해주고 출력
print(res)

# 이렇게도 가능
# for x in stack:
#     print(x,end = '')