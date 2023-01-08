def solution(board, moves):
    answer = 0
    tong = [0,0]
    
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                tong.append(board[i][m-1])
                board[i][m-1] = 0
                break
                
        if tong[-1] == tong[-2] and tong[-1] != 0 and tong[-2] != 0:
            tong.pop()
            tong.pop()
            answer += 2
            
    return answer