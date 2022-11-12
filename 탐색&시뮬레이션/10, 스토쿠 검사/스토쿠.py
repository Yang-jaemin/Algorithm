a = [list(map(int,input.split())) for _ in range(9)]

def check(tmp):
    # 행과 열 탐색
    for i in range(9):
        ch1 = [0]*10 # 0~9 까지의 인덱스 위해 # 행 체크
        ch2 = [0]*10                      # 열 체크
        for j in range(9):
            ch1[tmp[i][j]] = 1
            ch2[tmp[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    
    # 그룹탐색
    for i in range(3): # 행
        for j in range(3): # 열
            ch3 = [0]*10 # 그룹체크 , 합이 9인지 확인후 초기화 (같은 라인)
            for k in range(3):
                for s in range(3):
                    ch3[[tmp[i*3+k]]][a[j*3+s]]] = 1
            if ch3 != 9:
                return False
    
    return True
                        
            
          