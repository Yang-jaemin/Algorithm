def solution(s):
    a = []
    for i in s:
        a.append(i)
        
    if a[0]=='+':
        answer = int("".join(a[1:]))
    elif a[0]=='-':
        answer = -(int("".join(a[1:])))
    else: 
        answer = int("".join(a))
        
    return answer

print(solution('12345133123'))