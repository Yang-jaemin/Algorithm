# 666, 1666, 2666 ..,,,,
# 11666,12666,13666,14666,,,,
# 21666
# 그냥 다돌려봐
n = int(input())
first = 666
while True:  # 일단 돌아
    if '666' in str(first): # 만약 first안에 666이 있으면 
        n = n-1             # 순서에서 1개 까고
        if n == 0:          # 0이라는 건 그 순서가 됐다는 거니까
            print(first)    # 그수를 출력하고   
            break           # 탈출
    first = first+1         # 만약 그 순서가 아니라면 first에다가 +1 하고 다시 돌아

    
