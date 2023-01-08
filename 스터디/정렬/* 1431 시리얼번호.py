n = int(input())
guitar = []
for _ in range(n):
    s = input()
    
    # 자리수의 합
    summ = 0
    for i in s: # 들어온 문자열 하나하나 본다
        if i.isdigit(): # 숫자면 
            summ += int(i)  # 더해
    guitar.append((s,summ)) # 튜플로 정렬
    
guitar.sort(key=lambda x:(len(x[0]),x[1],x[0]))  # (길이, 숫자, 사전순)으로 정리하라고 lambda를 통해서 sorting

for i in guitar:
    print(i[0])
            

                
        
        
    
    