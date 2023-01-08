# 실패
def press(num,string):
    cnt = 0
    start = 0
    e = ''
    aa = string[start:num]   
    for i in range(0,len(string),num):
        if i+num > len(string):
            e += string[i:]
            break
        if aa == string[i:i+num]:
            cnt+=1
        else:
            if cnt != 1:
                e += (str(cnt)+aa)
                aa = string[i:i+num]
                cnt = 1
            else:
                e += aa
                aa = string[i:i+num]
                cnt = 1
    return len(e)

s = 'aabbaccc'
a = []
for i in range(1,len(s)+1):
    a.append(press(i,s))
answer = min(a)
print(answer)



def press(num,string):
    cnt = 0
    start = 0
    e = ''
    aa = string[:num]
    #print(aa)
    print(f'### {num} ###')
    for i in range(0,len(string),num):
        #if i+num >= len(string):
        #    e += string[i:]
        #    break
        #print(aa, string[i:i+num])
        if aa == string[i:min(i+num, len(string))]:
            cnt+=1
        else:
            if cnt != 1:
                e += (str(cnt)+aa)
            else:
                e += aa
            aa = string[i:i+num]
            cnt = 1
    if cnt != 1:
        e += (str(cnt)+aa)
    else:
        e += aa
    print(e)
    return len(e)

def solution(s):
    a = []
    for i in range(1,len(s)+1):
        a.append(press(i,s))
        answer = min(a)
    return answer




def solution(s):
    n = len(s)
    answer = 100000000
    for l in range(1, n+1): # l 은 나눌 문자 갯수
        ns = [s[i:i+l] for i in range(0, n, l)]
        #print(ns)
        
        cnt = 0 # l 로 나눴을 때의 답
        pv = ns[0] # 이전 값
        pvc = 1
        #res = ''
        for v in ns[1:]:
            if pv == v:
                pvc += 1
            else:
                if pvc > 1:
                    cnt += len(str(pvc))
                    #res += str(pvc)
                cnt += len(pv)
                #res += pv
                pv = v
                pvc = 1
        if pvc > 1:
            cnt += len(str(pvc))
            #res += str(pvc)
        cnt += len(pv)
        #res += pv
        #print(res, cnt)
        answer = min(answer, cnt)
    return answer