from collections import deque
n , m = map(int,input().split())
Q = [(pos,val) for pos,val in enumerate(list(map(int,input().split())))] #[(0, 12), (1, 34), (2, 12), (3, 34), (4, 55)] 이런식으로 받아씀
Q = deque(Q) # deque로 바꿔줌
cnt = 0
while True:
    cur = Q.popleft() # 앞에서 먼저빼고
    if any(cur[0]<x[0] for x in Q): # 만약 하나라도 true이면 실행 any 함수
        Q.append(cur)               # 큰게 있다면 뒤로 다시 넣음
    else:                           # 만약에 내 뒤에 위험도 큰사람이 없어 그러면
        cnt+=1                      # 진료 받고
        if cur[0] == m:             # m번째 환자면
            print(cnt)              # 몇번째로 진료 받았는지 출력 ㄲ
            break