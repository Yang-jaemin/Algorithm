import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호를 만나면
        i += 1 
        while word[i] != ">":      # 닫힌 괄호를 만날 때 까지
            i += 1 
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i] # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i+=1                # 그냥 증가시킨다

print("".join(word))
        

###########################################################
import sys

def convert(word, tag_mode):
  return ''.join(word if tag_mode else word[::-1])

s = sys.stdin.readline().rstrip()

tag_mode = False
ans = []
cur_word = []
for c in s:
  if c == '<':
    ans.append(convert(cur_word, tag_mode))
    ans.append('<')
    cur_word = []
    tag_mode = True
  elif c == '>':
    ans.append(convert(cur_word, tag_mode))
    ans.append('>')
    cur_word = []
    tag_mode = False
  elif c == ' ':
    ans.append(convert(cur_word, tag_mode))
    ans.append(' ')
    cur_word = []
  else:
    cur_word.append(c)
ans.append(''.join(cur_word[::-1]))

print("".join(ans))

# <ab cd>ef gh<ij kl>
# ['<', 'ab', ' ', 'cd', 'fe' ...]
# cur_word = [a,b]