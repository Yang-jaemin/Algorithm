# 내가 배운 방식인데 메모리가 초과,,
# N = int(input())
# A = list(range(1,N+1))

# lt = 0
# rt = 1
# res = A[lt]
# cnt = 0 
# while True:
#     if res < N:
#         if lt < N:
#             res = res+A[rt]
#             rt+=1
#         else:
#             break
#     elif res > N:
#         res = res - A[lt]
#         lt+=1
#     else:
#         cnt+=1
#         res = res -A[lt]
#         lt+=1
# print(cnt)

# 책 방식
# 맨마지막의 15는 이미 계산해서 cnt +1 그리고 처음에 1을 포함하고 시작
N = int(input())
start_index = 1
end_index = 1
sum = 1
cnt = 1
while end_index != N:
    if sum == N:
        cnt += 1
        end_index += 1
        sum += end_index
    elif sum > N:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index
print(cnt)