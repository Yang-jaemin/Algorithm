k,m = 4,3
score = [4,1,2,2,4,4,4,4,1,2,4,2]
def solution(k,m,score):
    score.sort()
    summ = 0
    if len(score) >= m:
        while len(score) >= m:
            box = []
            for _ in range(m):
                box.append(score.pop())
            summ += (min(box)*m)
    else:
        return summ
    return summ

        