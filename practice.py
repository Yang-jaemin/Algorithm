s = 'sdfjkw'
n = 4
answer = ''
for i in s:
    if i == 'z':
        i = 'a'
        n = n-1
    elif i == ' ':
        answer += ' '
        continue
    elif 90 < ord(i)+n < 97:
        n = n+6
    answer += chr(ord(i)+n)
print(answer)