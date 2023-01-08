def solution(t, p):
    pp = len(p)
    cnt = 0
    for i in range(len(t)):
        s = i
        e = s+pp
        if e <= len(t):
            if int(t[s:e]) <= int(p):
                cnt += 1
    return cnt