def solution(s):
    s = list(s)
    answer = 0
    for i in range(1,len(s)+1):
        a = 0
        b = i+a
        while b <= len(s):
            tmp = s[a:b]
            if len(tmp) != 0:
                if tmp[0] == tmp[-1]:
                    if tmp == tmp[::-1]:
                        if len(tmp) > answer:
                            answer = len(tmp)
            a += 1
            b += 1
    return answer
print(solution("abcdcba"))
    