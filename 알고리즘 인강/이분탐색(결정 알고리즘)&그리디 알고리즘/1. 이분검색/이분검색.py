n  = 8
m = 32
l = [23,87,65,12,57,32,99,81]
# 이분검색은  lt 랑 rt 즉, 포인트 변수가 필요함 또는 정렬된 자료 필요
# mid = (lt+rt)//2 (3)
# a[mid]가 m이냐?? 그러면 mid +1 이답
# 아니면? a[mid]가 내가 찾는 값보다 크다 그러면 mid보다 작아야한다.
# ->> rt = mid -1 작으면 lt = mid +1
lt = 0
rt = n-1

l.sort()

while lt <= rt:
    mid = (lt+rt)//2
    if l[mid] > m:
        rt = mid-1
    elif l[mid] < m:
        lt = mid+1
    else:
        print(mid+1)
        break