def dvd(mb):
    cnt = 1 
    sum = 0
    for x in li:
        if sum + x > mb:
            cnt += 1
            sum = x # 다시 초기화를 해줘야하니까 x부터 다시 더해주기 위해서 sum에 x를 넣어용
        else: 
            sum +=x
    return cnt
    
n , m = map(int,input().split())
li = list(map(int,input().split()))
maxx = max(li)
lt = 1
rt = sum(li)
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if mid > maxx and dvd(mid) <= m: # mid > maxx 하는 이유는 노래를 자를 수가 없으니까 가장 긴노래보단 용량이 커야함 (반례수정)
        res = mid
        rt = mid-1
    else:
        lt = mid+1

print(res)