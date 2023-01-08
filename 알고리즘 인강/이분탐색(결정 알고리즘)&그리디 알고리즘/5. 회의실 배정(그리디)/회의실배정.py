# 그리디 알고리즘 : 문제를 푸는 과정에서 단계에서 제일 좋은 답을 선택(그리디는 결국 정렬)
n = int(input())
meet = []
for i in range(n):
    s,e = map(int,input().split())
    meet.append((s,e)) # 시작시간과 끝나는 시간을 튜플형태로 넣는다

meet.sort(key = lambda x : (x[1], x[0])) # key를 지정해준다. x는 meet의 데이터를 하나씩 받는 매개변수 같은 거라고 생각 하고 (x[1]:x[0]) x[1]을 우선으로 고려, 안하면 앞의 값 정렬

et = 0 # 회의 끝나는 시간
cnt = 0
for s, e in meet:
    if s>= et: # 처음에는 0이니까 첫 회의는 무조건함
        cnt+=1
        et = e
print(cnt)