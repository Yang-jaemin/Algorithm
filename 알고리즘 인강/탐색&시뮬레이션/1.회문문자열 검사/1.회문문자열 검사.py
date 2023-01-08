# 회문문자열 : 앞으로 읽나 뒤로 읽나 같음,회문문자열이면 yes 아니면 No
n = int(input())


for i in range(n):
    s = input()
    s = s.upper()
    for j in range(len(s)//2):
        if s[j] != s[-1-j]:
            print('#%d No' %(i+1))
            break
    else: 
        print('#%d Yes' %(i+1))
        

# 다른 코드
n = int(input())


for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1] # 거꾸로된 문자열: 슬라이싱
        print('#%d Yes' %(i+1))
    else:
        print('#%d No' %(i+1))



    

    

