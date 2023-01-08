T = int(input()) # 테스트할 케이스가 몇개인지 입력 받음

for t in range(T):                     
 # T = 2 라면 0 1 총 2번 돈다 
    N, s, e, k = map(int,input().split())
    # 분리해서 각 변수에 int형으로 저장
    a  = list(map(int,input().split()))
    # N개의 숫자를 받아서 int형으로 저장후 리스트 화
    a = a[s-1:e] 
    # 2번째면 인덱스 번호는 1이니까 s-1 , 5번째는 인덱스 번호는 4 근데 어차피 e의 전까지 슬라이싱
    a.sort()
    # 오름차순 sort
    print("#%d %d" %(t+1,a[k-1])) 
    # 출력형식 지키기 위해서 t+1을 해주었고 k번째 숫자이니까 인덱스 고려해서 a[k-1]