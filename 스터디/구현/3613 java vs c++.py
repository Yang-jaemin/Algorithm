# 54퍼에서 실패 반례 생각이 안남..

n = input()
bb = True
error = False
new = ''
if '_' in n:  # c++ 일때
    if n[0] == '_' or n[-1] == '_':  # 맨 뒤 문자가 '_' 이면 에러, 맨 앞 문자가 '_' 이면 에러
        error = True
        
    for i in range(len(n)):
        if i+1 < len(n):
            if n[i] == n[i+1] == '_': # '_' 연속 두개면 에러
                error = True
        if n[i].isupper():            # 맨 앞 문자가 대문자면 에러
            error = True
        if n[i] == '_':
            bb = False
        else:
            if bb:
                new += n[i]
            else:
                new += n[i].upper()
                bb = True
else:        # java 일때
    if n[0].isupper():  # 맨 앞 문자 대문자면 에러
        error = True
        
    for i in range(len(n)):
        if n[i] == ' ':    # 공백 발견시 에러
            error = True
            
        if n[i].isupper():
            new += n[i].lower() 
        else:
            new += n[i]
            
        if i+1 < len(n) :    
            if n[i+1].isupper():
                new += '_'
if error:
    print('Error!')
else:
    print(new)