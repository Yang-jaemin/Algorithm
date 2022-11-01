s = '3+5*2/(7-2)'
stack = []
res = '' # 여기로 출력

for x in s:
    if x.isdecimal(): # 10진수 숫자인지 판단가능
        res += x      #  숫자면 res에 누적
    else:             # 숫자가 아니라 연산자라면
        if x == '(':  # 여는 괄호면?
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1]=='*' or stack[-1] == '/'): # 우선순위 고려, stack 안에 있는 연산자가 우선순위가 같을 경우만
                res += stack.pop()                                # stack에 들어가있는 *이나 /를 빼고
            stack.append(x)                                       # *이나 /를 넣는다
        elif x == '+' or x == '-':                      
            while stack and stack[-1]!='(':     # 만약 괄호안에 있는게 아니라면 앞의 연산자를 stack에서 빼고
                res += stack.pop()
            stack.append(x)                     # 그 뒤에 자기가 들어감
        elif x == ')':
            while stack and stack[-1]!= '(':    # 만약 닫는 괄호가 나온다면 여는 괄호 전까지 다 pop시키고
                res += stack.pop()
            stack.pop()                         # 여는 괄호 pop해서 버림
while stack:
    res += stack.pop()
print(res)
      