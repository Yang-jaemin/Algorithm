# https://school.programmers.co.kr/learn/courses/30/lessons/12907
def solution(n, money):
    dy = [0]*(n+1)
    dy[0] = 1
    for coin in money:
        for y in range(coin,n+1):
            dy[y] += dy[y-coin] 
            dy[y] %= 1000000007  # 모듈러 연산
                                 # 왜써야하냐, dy[y]가 너무 커지면 계산안댐(파이썬은 가능)
            # 일단 코인 이 1일때 y가 1부터 5까지 도는데
            # 그러면 1을 사용해서 y를 만들 수 있는 경우가 dy[1~5]에 저장
            #     코인이 2일때 y가 2부터 5까지 도는데
            # 그러면 2를 사용해서 y를 만들 수 있는 경우를 저장해야하지
            # 근데 이미 dy[1~5]까지에 1로만 만들 수 있는게 저장
            # 그러면 dy[2~5]에 dy[2,3,4,5-2]를 
            # dy[2] += d[2-2]
            # dy[3] += dy[3-2]
            # dy[4] += dy[4-2].. 이렇게 들어가는데
            # 예를 들어 dy[4] 즉 4를 1로만 만드는 경우가 이미 들어가있었고
            # 이제 2를 함께 사용했을때의 경우를 넣어야한다. 근데 dy[4-2]를 더해주면(2를 사용한다고 무조건으로 치는거임)
            # dy[4] = 1(1로만 만듬)+dy[2](2를 무조건 사용한다고 했을때 나머지인 2를 1과2를 섞어서 사용하는 조합)을 넣어줌
            
            # 예를 들어 코인이 4라면 y가 5라면
            # dy[5] += dy[5-4] 이식의 의미는 4를 무조건 사용하니까 5에서 4를 뺀 1의 경우의 수만 더 더해주면 된다 라는거임
    return dy[y]


# https://hwayomingdlog.tistory.com/100 (시간복잡도 살짝 틀림)
# https://www.geeksforgeeks.org/coin-change-dp-7/
#
# f(m, i) = m번째 까지의 동전들을 사용해서 i원 을 만들 수 있는 가짓수 = f(m-1, i) + f(m, i-money[m])

# f(a, b) = ?    - dp[1]dp[2]dp[3] = 1
#                  dp[2] 1+1 dp[3] 
# 1 2 5
#    |0 1 2 3 4 5
# ---+-----------
# 1 0|1 1 1 1 1 1
# 2 1|1 1 2 2 3 4
# 5 2|1 1 2 2 3 4

# TSP(Traveling Salesman Problem)
# 개발자 프론트 ,백앤드
# AWS
# V1

def solution(n, money):
    dp = [[1] + [0] * n for _ in range(len(money))]
    for m in range(len(money)):
        for i in range(1, n+1):
            if m > 0:
                dp[m][i] = dp[m-1][i]
            if i >= money[m]:
                dp[m][i] += dp[m][i-money[m]]
                dp[m][i] %= 1000000007
    return dp[-1][n]

# V2
def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1
    for m in money:
        for i in range(0, n+1):
            if i < m:
                continue
            dp[i] += dp[i-m]
            dp[i] %= 1000000007
    return dp[n]