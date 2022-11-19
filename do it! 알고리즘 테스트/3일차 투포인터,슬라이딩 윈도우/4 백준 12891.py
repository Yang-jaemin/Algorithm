n,m = map(int,input().split())
s = list(input())
a,c,g,t = map(int,input().split())
i = 0
j = m
cnt = 0
for _ in range(len(s)-m+1):
    S = s[i:j]
    if S.count('A') == a:
        if S.count('C') == c:
            if S.count('G') == g:
                if S.count('T') == t:
                     cnt +=1
    i += 1
    j += 1
    
print(cnt)
     
    