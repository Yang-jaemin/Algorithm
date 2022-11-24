# 내가 짠 코드
# n,m = map(int,input().split())
# s = list(input())
# a,c,g,t = map(int,input().split())
# i = 0
# j = m
# cnt = 0
# for _ in range(len(s)-m+1):
#     S = s[i:j]
#     if S.count('A') == a:
#         if S.count('C') == c:
#             if S.count('G') == g:
#                 if S.count('T') == t:
#                      cnt +=1
#     i += 1
#     j += 1
    
# print(cnt)
     
# 책의 코드
# 슈도코드
# check 리스트 생성 - 비밀번호 체크리스트(조건)
check = [0]*4
# mylist - 현재 상태리스트(현재 윈도우의 조건)   
mylist = [0]*4
# check_secret
check_secret = 0
# 함수정의
def myadd(c):
    global check_secret
    if c == 'A':
        mylist[0] += 1  # 만약 c가 A이면 A자리 +1
        if mylist[0] == check[0]: # 그리고 내 A의 개수랑 check의 A개수가 맞으면 check_secret +=1
            check_secret += 1 
    elif c == 'C':
        mylist[1] += 1  # 만약 c가 C이면 C자리 +1
        if mylist[1] == check[1]: # 그리고 내 C의 개수랑 check의 C개수가 맞으면 check_secret +=1
            check_secret += 1
    elif c == 'G':
        mylist[2] += 1  # 만약 c가 C이면 C자리 +1
        if mylist[2] == check[2]: # 그리고 내 C의 개수랑 check의 C개수가 맞으면 check_secret +=1
            check_secret += 1
    elif c == 'T':
        mylist[3] += 1  # 만약 c가 C이면 C자리 +1
        if mylist[3] == check[3]: # 그리고 내 C의 개수랑 check의 C개수가 맞으면 check_secret +=1
            check_secret += 1
            
def myremove(c):
    global check_secret
    if c == 'A':
        if mylist[0] == check[0]:
            check_secret -= 1
        mylist[0] -= 1
    elif c == 'C':
        if mylist[1] == check[1]:
            check_secret -= 1
        mylist[1] -= 1
    elif c == 'G':
        if mylist[2] == check[2]:
            check_secret -= 1
        mylist[2] -= 1
    elif c == 'T':
        if mylist[3] == check[3]:
            check_secret -= 1
        mylist[3] -= 1
        
            
S,P = map(int,input().split())
Result = 0
A = list(input()) # 문자열 받기
check = list(map(int,input().split()))
    
for i in range(4):
    if check[i] == 0:
        check_secret += 1 # 왜냐? 안들어가도 되는거니까 ㅇㅇ
    
for i in range(P):
    myadd(A[i])  

if check_secret == 4:
    Result += 1

for i in range(P,S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if check_secret == 4:
        Result += 1

print(Result)   