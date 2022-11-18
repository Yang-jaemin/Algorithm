# 책 50쪽 -> 아이디어가 존나 생각하기 힘듬 ㅇㅇㅇ 그래도 잘봐바 이해는 된다.
# 슈도코드
# n,m 받기
n,m = map(int,input().split())
# answer 만들기, sum 만들기, 합배열 만들기
answer = 0
sum = 0
s = [0] * n
# 원배열 a 입력 받고 리스트로
a = list(map(int,input().split()))
# 합배열 s 만들고
for i in range(n):
    sum = sum + a[i]
    s[i] = sum

# 합배열 s를 m으로 다 나누어주고(리뉴얼)
for j in range(n):
    s[j] = s[j]%m

# 리뉴얼 합배열에서 0인거 개수 센다. answer에 더해줘
for x in s:
    if x == 0:
        answer+=1
# 숫자가 같은거 개수센다.(이게 좀 빡셈)
for i in range(m):
    res = s.count(i)
    if res >1:
        answer += (res*(res-1))//2
print(answer)
# 조합으로 구하기