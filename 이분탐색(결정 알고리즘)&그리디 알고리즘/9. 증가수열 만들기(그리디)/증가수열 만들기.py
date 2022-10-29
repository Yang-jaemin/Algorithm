n = int(input())
a = list(map(int,input().split()))
lt = 0
rt = n-1 # 마지막 인덱스
last = 0 # 직전의 인덱스
res = '' # 문자 정렬 rll llr 이런거
tmp = []

while lt <= rt:
    if a[lt]> last:
        tmp.append((a[lt],'L')) # 일단 양옆 다 넣고
    if a[rt] > last:
        tmp.append((a[rt],'R'))
    tmp.sort()                  # sort -> 튜플 0번 기준으로 정렬
    if len(tmp) == 0:   # lt rt 모두 last보다 작아서 안들어가졌을때 종료
        break
    else:
        res = res+tmp[0][1] # 문자열을 더함 LLR 이렇게 RRL 이렇게
        last = tmp[0][0]    # tmp에 저장된 [0][0] 숫자가 라스트 더 큰 숫자는 [1][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(len(res))
print(res)
