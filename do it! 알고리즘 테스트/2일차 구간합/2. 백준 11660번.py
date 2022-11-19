# 구간합 구하기2
# 슈도 코드
# n, m 받기
# for n만큼 반복
# 2차원 리스트 저장

# for i를 n까지 반복:
# for j를 1부터 n까지 반복:
#  합배열 저장

# for m만큼 반복:
# 질의 입력받고
# 계산출력
# n,m = map(int,input().split())
# A = [[0]*(n+1)] # 원본 리스트
# D = [[0]*(n+1) for _ in range(n+1)] # 합배열
# for _ in range(n):
#     A_row =  [0]+[int(x) for x in input().split()]
#     A.append(A_row)

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         D[i][j] = D[i][j-1]+D[i-1][j]-D[i-1][j-1]+A[i][j] # 합배열 저장

# for _ in range(m):
#     s1,e1,s2,e2 = map(int,input().split())
#     res = D[s2][e2]-D[s1-1][e1]-D[s1][e1-1]-D[s1-1][e1-1]
#     print(res)
n,m = map(int,input().split())
A = [[0]*(n+1)] # [0,0,0,0,0,0,0]
D = [[0]*(n+1) for _ in range(n+1)] # 합배열
for _ in range(n):
    A_row = [0]+ [int(x) for x in input().split()] # [0,1,2,3,4]
    A.append(A_row) 

for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1]+A[i][j] # 합배열!!!!!!!! 제발 완료

for _ in range(m):
    y1,x1,y2,x2 = map(int,input().split())
    res = D[y2][x2]-D[y2][x1-1]-D[y1-1][x2]+D[y1-1][x1-1]
    print(res)