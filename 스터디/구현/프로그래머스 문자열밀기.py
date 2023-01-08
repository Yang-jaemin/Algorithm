# https://school.programmers.co.kr/learn/courses/30/lessons/120921
def solution(A, B):
    cnt = 0
    for _ in range(len(A)):
        if A == B:
            answer = 0
            break
        A = A[-1] + A[:-1]
        cnt += 1
        if A == B:
            answer = cnt
            break
        else:
            answer = -1

    return answer