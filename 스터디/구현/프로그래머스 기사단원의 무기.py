def yak(n):
    cnt = 0 
    for i in range(1,int(n**(1/2)+1)):  # 시간복잡도를 줄여서 약수 계산하기 int(n**(1/2)+1)
        if n % i == 0:
            cnt += 1
            if i**2 != n:
                cnt += 1
    return cnt
        
# N^1.5
def solution(number, limit, power):
    answer = 0
    weapon = []
    for j in range(1, number+1):
        weapon.append(yak(j))
  
    for k in range(len(weapon)):
        if weapon[k] <= limit:
            answer += weapon[k]
        else:
            answer += power
        
    return answer