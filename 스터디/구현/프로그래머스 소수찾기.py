from itertools import permutations
def sosu(x):
    if x == 0 or x == 1:
        return False
        
    for i in range (2, int(x**(1/2) + 1)):	# 2부터 x의 제곱근까지의 숫자
    	if x % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
        	return False
    else:
        return 	True
    
def solution(numbers):
    number = list(numbers) # permutation 돌리기 위해서 list로 바꿔줌
    cnt = 0
    a = []
    f = set() # 중복 지우기위해 set사용
    for k in range(1,len(number)+1): # 1부터 전체 길이까지의 순열을 구해야해서 for 문
        a = permutations(numbers,k)  # 길이 k의 순열 저장
        for m in a:
            f.add(int(''.join(m)))   # f에 list-> 문자열 -> int로 바꿔서 넣기

    for p in f:     # f에는 모든 경우의 숫자가 중복없이 들어가있음
        if sosu(p): # 소수판별
            cnt+=1
    return cnt