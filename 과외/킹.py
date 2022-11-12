# 입력을 문자로 받으니까 A1 이렇게 주면 A를 좌표로 사용가능하게 바꿔야겠다.
# 오 왼 뒤 앞 좌표로 구현하면 될듯 .. 딕셔너리..?

king, stone, n = input().split()
k = list(map(int, [ord(king[0]) - 64, king[1]]))
s = list(map(int, [ord(stone[0]) - 64, stone[1]]))
move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

for _ in range(int(n)):
    m = input()
    kx = k[0] + move[m][0]
    ky = k[1] + move[m][1] # 움직이기