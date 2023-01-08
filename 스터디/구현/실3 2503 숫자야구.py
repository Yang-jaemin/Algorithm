from itertools import permutations
data = list(permutations(['1','2','3','4','5','6','7','8','9'],3))  # 3자리로 만들수 있는 순열 다만듬
n = int(input())    # 몇개의 경우가 있는지(테스트)
removecount = 0     # data에서 remove하면서 개수가 줄어드니까 2개 줄어들면 i-2해서 무조건 앞에서부터 탐색하게
for _ in range(n):  # n번 돌기
    num,s,b = map(int,input().split()) # 숫자랑 스트라이크 볼 나옴
    num = list(str(num))        # 숫자를 리스트화 345 => ['3','4','5']
    removecount = 0             # 숫자가 새로 입력될 때 마다 removecount 0으로 초기화
    for i in range(len(data)):  # data에서 하나씩 비교
        strike = 0
        ball = 0
        i = i - removecount
        for j in range(3):
            if num[j] == data[i][j]:  # data 뽑은거에서 자리수 비교
                strike += 1           # 만약에 자리수끼리 같다면 strike +1
            elif num[j] in data[i]:   # 자리수 끼리 같지는 않은데 그 num의 숫자들중하나가 이 data[i]의 숫자들중에 있다면
                ball += 1             # ball +1
            
        if (strike != s) or (ball != b):  # 만약 strike와 ball과 s,b가 하나라도 다르다면
            data.remove(data[i])          # 제거
            removecount += 1              # 1개 제거했으니까 인덱스 하나 당겨야지 (i-removecount)
            
print(len(data)) 
# 뺄거 다빼고 남은 데이터의 개수만 출력
                
                
        






































# from itertools import permutations
# data = list(permutations(['1','2','3','4','5','6','7','8','9'],3)) # 모든 3자리수를 data에 넣어 놓는다.
# n = int(input())
# RemoveCount = 0
# for _ in range(n):
#     num,s,b = map(int,input().split())
#     num = list(str(num))  # 리스트는 리스트끼리만 비교가되나??
#     RemoveCount = 0
#     for i in range(len(data)):
#         strike = ball = 0
#         i = i - RemoveCount
#         for j in range(3):
#             if num[j] == data[i][j]:
#                 strike += 1
#             elif num[j] in data[i]:
#                 ball += 1
            
#         if (strike != s) or (ball != b):
#             data.remove(data[i])
#             RemoveCount += 1
                
# print(len(data))


