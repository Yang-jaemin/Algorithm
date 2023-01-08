a = input()
b = input()
str1 = [0]*52 # 대소문자 합치면 52개니까
str2 = [0]*52 
for x in a:
    if x.isupper(): # 대문자면
        str1[ord(x)-65] += 1 # 대문자는 65번부터 ~~ ord 문자열 -> 아스키 넘버
    else:
        str1[ord(x)-71] += 1 # 소문자는 97부터~~ -71 해줘야 인덱스 26 부터 시작할 수있다
for x in b:
    if x.isupper(): # 대문자면
        str2[ord(x)-65] += 1 # 대문자는 65번부터 ~~ ord 문자열 -> 아스키 넘버
    else:
        str2[ord(x)-71] += 1 # 소문자는 97부터~~ -71 해줘야 인덱스 26 부터 시작할 수있다
        
for i in range(52): # 알파벳이 52개니까 인덱스도 0~51까지 이씀
    if str1[i] != str2[i]:
        print("no")
        break
else:
    print('Yes')        