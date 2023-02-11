# {{{}}} 
# def check(arr):
#     c1 = [0]*2  
#     c2 = [0]*2 
#     c3 = [0]*2
#     for c in arr:
#         if c == '[':
#             c1[0] = 1
#         elif c == ']':
#             if c1[0] == 0:
#                 return False
#             else:
#                 c1[1] = 1
#         elif c == '{':
#             c2[0] = 1
#         elif c == '}':
#             if c2[0] == 0:
#                 return False
#             else:
#                 c2[1] = 1
#         if c == '(':
#             c3[0] = 1
#         elif c == ')':
#             if c3[0] == 0:
#                 return False
#             else:
#                 c3[1] = 1
#     if sum(c1) == 0 or sum(c1) == 2:
#         if sum(c2) == 0 or sum(c2) == 2:
#             if sum(c3) == 0 or sum(c3) == 2:
#                 return True
#     return False
# def solution(s):
#     cnt = 0
#     for i in range(len(s)):
#         s = s[1:] + s[0]
#         # print(s)
#         if check(s):
#             cnt += 1
#     return cnt

# 30분        
        
def check(arr):
    stack = []

    #paren1 = {'(': ')', '[': ']'}
    #paren2 = {')': '(', ']': '['}

    for c in arr:
        #if c in paren2: # closer
        #    if len(stack) == 0:
        #        return False
        #    if stack[-1] != paren2[c]:
        #        return False
        #    else:
        #        stack.pop()
        #else: # opener
        #    stack.append(c)
            
        if c == ']':
            if len(stack) == 0:
                return False
            if stack[-1] != '[':
                return False
            else:
                stack.pop()
        elif c == '}':
            if len(stack) == 0:
                return False
            if stack[-1] != '{':
                return False
            else:
                stack.pop()
        elif c == ')':
            if len(stack) == 0:
                return False
            if stack[-1] != '(':
                return False
            else:
                stack.pop()
        else:
            stack.append(c)
    if len(stack) != 0:
        return False
    else:
        return True

def solution(s):
    cnt = 0
    for _ in range(len(s)):
        s = s[1:] + s[0]
        if check(s):
            cnt += 1
    return cnt

# 괄호의 종류는 입력에서 주어지는 경우
# ['{}', '[]', '<>']
# ['{}', '[]', '()']
# data-driven programming