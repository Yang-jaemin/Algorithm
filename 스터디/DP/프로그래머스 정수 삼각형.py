def solution(triangle):
    answer = 0
    triangle = [[0]+t+[0] for t in triangle]  # 인덱스 에러 없애기위햐서 양모서리에 0추가 # 센티널
    for i in range(1,len(triangle)):
        for j in range(1,i+2):
            triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j]) # 왼위 오위 비교해서 큰애를 더해
    answer = max(triangle[len(triangle)-1]) # 막줄에서 젤큰애
                        # triangle[-1]
    return answer


def solution(triangle):
    dp = [[0] * (i+1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j < i:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + triangle[i][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + triangle[i][j])

    return max(dp[-1])

# t = [
#   [0],
#   [0, 0],
#   [0, 0, 0],
#  ]

# t[len(t)-1] => [0, 0, 0]
# t[0] => [0]