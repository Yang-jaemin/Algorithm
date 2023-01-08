def solution(brown, yellow):
    half_brown = brown//2
    for i in range(1,half_brown):
        for j in range(1,half_brown):
            if i+j == half_brown and (i-2)*(j) == yellow:
                if i >= (j+2):
                    answer = [i,j+2]
                    break
    return answer