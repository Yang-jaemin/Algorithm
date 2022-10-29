n, h = map(int,input().split())
line = []
for _ in range(n):
    tmp = int(input())
    line.append(tmp)
line.sort()

lt = 1
rt = line[n-1]
res = 0

def count(len):
    cnt = 1
    ep = line[0] # 말이 마지막으로 배치된 지점 / 배치 됐으니까 cnt가 +1
    for i in range(1,n):
        if (line[i]-ep) >= len:
            cnt+=1
            ep = line[i]
    return cnt

# 이분탐색
while lt <= rt:
    
    mid = (rt+lt)//2
    
    if count(mid) >= h:
        res = mid
        lt = mid+1
    else:
        rt = mid-1