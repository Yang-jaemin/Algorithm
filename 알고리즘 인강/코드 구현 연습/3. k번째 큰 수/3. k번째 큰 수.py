n, k = map(int,input().split()) # n은 카드 몇장 가지고 있나

a = list(map(int,input().split())) # n개의 숫자 입력 리스트로 받기

res = set( )           
# 중복제거 set은 중복은 하나로 처리

for i in range(n):                  # 3장을 뽑을 수 있는 모든 경우의 수를 구하는 방법 3중 for문
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m]) # 모든 경우가 set에 저장(중복 제외)
        
res = list(res)                 # 내림차순(sort reverse)를 하기 위해서 다시 리스트로
res.sort(reverse=True)          # 내림차순
print(res[k-1])                 # k번째 수 출력
            
    