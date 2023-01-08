a = '352+*9-'
stack =[]
for x in a:
    if x.isdecimal():
        stack.append(int(x)) # 처음에는 문자열 상태니까 연산하려면 int 화를 해줘야한다.
    else:
        if x == '+' :
            w = stack.pop()
            q = stack.pop()
            stack.append(q+w)
        elif x == '-':
            w = stack.pop()
            q = stack.pop()
            stack.append(q-w)
        elif x == '*':
            w = stack.pop()
            q = stack.pop()
            stack.append(q*w)
        else:
            w = stack.pop()
            q = stack.pop()
            stack.append(q/w)
print(stack[0])
            
        