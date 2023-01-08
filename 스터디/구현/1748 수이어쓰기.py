N = int(input())
answer = 0
length_N = len(str(N))
for i in range(1,length_N):
    answer += 9*(10**(i-1))*i   # 규칙 찾았음 1 x 9 x 1, 9 x 10 x 2 , 9 x 100 x 3 ....
answer += (N -(10**(length_N-1)-1))*length_N  # 마지막 남은거
print(answer) 