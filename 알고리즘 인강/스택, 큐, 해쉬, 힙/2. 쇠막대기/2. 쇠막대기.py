s = input()  # ()(((()())(())()))(())
stack =[]
cnt = 0
for i in range(len(s)):     # 괄호 전체 탐색위해서
    if s[i] == '(':         # 만약에 여는 괄호면 
        stack.append(s[i])  # 스택 맨뒤에 append
    else:
        if s[i-1] == '(': # s[i]가 닫는 괄호인 상황에서는 그 바로뒤가 어떤괄호인지 알아야함[ s[i-1] ]
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1