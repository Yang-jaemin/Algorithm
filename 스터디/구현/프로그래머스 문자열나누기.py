# https://school.programmers.co.kr/learn/courses/30/lessons/140108
def solution(s):
    x_cnt = 0
    nx_cnt = 0
    answer = 0
    bb = True
    while bb:
        x = s[0]
        x_cnt = 1
        if len(s) == 1:
            bb = False
        for i in range(1,len(s)):
            if s[i] == x:
                x_cnt += 1
            else:
                nx_cnt += 1
            
            if x_cnt == nx_cnt:   # for 문중에 여기에 걸리게되면(숫자가 같을떄) 마지막 루프(뒤에 나눌 문자가 없음)
                if i+1 == len(s): # 마지막까지 인덱스가 도달 했을때는 더 분리 못하니까 False로 바꿔준다.
                    bb = False
                else:           # 정상적으로 나누어줌
                    s = s[i+1:] # O(N)
                    answer += 1
                    x_cnt = 0
                    nx_cnt = 0
                break
        else:  # for문이 다돌았는데도 숫자가 같은 경우가 안생기면 그냥 끝내버리자
            break
                
    return (answer+1) # +1은 마지막에 남은 덩이도 세주어야하기때문


def solution(s):
    answer = 0
    # j = 0
    while bb:
        x = s[0]
        x_cnt = 1
        nx_cnt = 0
        if len(s) == 1:
            bb = False
        for i in range(1,len(s)):
            if s[j+i] == x:
                x_cnt += 1
            else:
                nx_cnt += 1
            
            if x_cnt == nx_cnt:   # for 문중에 여기에 걸리게되면(숫자가 같을떄) 마지막 루프(뒤에 나눌 문자가 없음)
                if j+i+1 == len(s): # 마지막까지 인덱스가 도달 했을때는 더 분리 못하니까 False로 바꿔준다.
                    bb = False
                else:           # 정상적으로 나누어줌
                    # j = j+i
                    answer += 1
                break
        else:  # for문이 다돌았는데도 숫자가 같은 경우가 안생기면 그냥 끝내버리자
            break
                
    return (answer+1) # +1은 마지막에 남은 덩이도 세주어야하기때문