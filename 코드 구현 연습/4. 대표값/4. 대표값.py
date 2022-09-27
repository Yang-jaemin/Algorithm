##  복습 요망

n = map(int,input()) # 몇명인지 입력받기
a = list(map(int,input().split())) # 학생들의 점수를 리스트로 입력받기

avr = sum(a)/n  # sum(a) : list a의 값들을 모두 더해준다.

# 반올림 하기
avr += 0.5
avr = int(avr)

# 최솟값 구하기
min = int('inf')
for index, x in enumerate(a):  # enumerate(a) : index와 값을 같이 출력해준다.(변수 2개)
    tmp = abs(x-avr)           # abs() : 절댓값 함수
    if tmp <  min :
        min = tmp
        score = x
        res = index + 1 # 0부터 index가 시작이니까 +1
    
    elif tmp == min:  # 평균이 74이고 [73,75,75] 로 있을때 tmp는 같지만 75가 더 크니까 75가 score
        if x > score: # 뒤에도 75가 있지만 =가 없으니까 앞에 있는 값이 답이 된다. *[선수과제] 최솟값 참고
            score = x
            res = index + 1  
        
print(avr,res)