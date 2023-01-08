def recursion(s, l, r):
    global cnt
    if l >= r:
        print(1,cnt)
        return
    elif s[l] != s[r]: 
        print(0,cnt)
        return
    else:
        cnt += 1 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(int(input())):
    cnt = 1
    a = input()
    isPalindrome(a)