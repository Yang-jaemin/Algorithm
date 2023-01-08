# https://school.programmers.co.kr/learn/courses/30/lessons/12915
def solution(strings, n):
    new_strings = []
    tmp = []
    for a in strings:
        tmp.append((a,a[n]))
    tmp.sort(key = lambda x : (x[1],x[0]))
    for b,c in tmp:
        new_strings.append(b)
    
    return new_strings



def solution(strings, n):
    new_strings = []
    tmp = []
    for a in strings:
        tmp.append((a[n], a))
    tmp.sort()
    for c,b in tmp:
        new_strings.append(b)
    
    return new_strings

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))



# ["sun",        "bed",        "car"]
# [("u", "sun"), ("e", "bed"), ("a", "car")]
# ["car", "bed", "sun"]