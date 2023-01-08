k,n = map(int,input().split())
li = [] #[802,743,457,539] # 범위는 여기에서 제일 긴거 , 가장큰 길이보단 짧다 1~802가 첫 시작 범위
answer = 0
largest = 0 # 리스트에서 가장 큰 수 저장위해서

def Count(len):
    cnt = 0
    for x in li:
        cnt += (x//len)
    return cnt
    
for i in range(k):
    tmp = int(input())
    li.append(tmp) # 뒤에서부터 들어간다.
    largest = max(largest,tmp) # 큰값 largest에 넣기
lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n: # count는 갯수를 리턴할거야
        res = mid
        lt = mid+1 # mid가 완벽한 길이보다는 짧아 그래서 좀 늘려줘야해
    else: # mid의 길이가 너무긴거야 그러니까 rt를 줄여줘야지
        rt = mid-1
print(res)

    