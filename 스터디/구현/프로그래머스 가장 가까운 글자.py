s = 'foobar'
answer = []
s = list(s)
rs = s[::-1]
print(rs)
bb = True
for i in range(len(s)):
    bb = True
    for j in range(len(s)-i,len(s)):
        if rs[j] == s[i]:
            answer.append(j-(len(s)-i-1))
            bb = False
            break
    else:
        if bb:
            answer.append(-1)
            
                
print(answer)