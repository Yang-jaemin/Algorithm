def solution(rows, columns, queries):
    a = []
    board = []
    answer = []
    start = 1
    # board 만들기
    for _ in range(rows): 
        for j in range(start ,columns+start):
            a.append(j)
        start += columns
        board.append(a)
        a = []
    
    for q in queries:
        query = []
        for d in q:
            query.append(d-1) # 행렬에 맞게 1 빼줌
        
            #왼쪽 위 임시저장
        tmp = board[query[0]][query[1]]
        small = tmp
        
        # 왼
        for i in range(query[0]+1,query[2]+1):
            board[i-1][query[1]] = board[i][query[1]]
            small = min(small,board[i][query[1]])
        # 밑
        for i in range(query[1]+1,query[3]+1):
            board[query[2]][i-1] = board[query[2]][i] 
            small = min(small,board[query[2]][i])
        # 오
        for i in range(query[2]-1,query[0]-1,-1):
            board[i+1][query[3]] = board[i][query[3]]
            small = min(small,board[i][query[3]])
        # 밑
        for i in range(query[3]-1,query[1]-1,-1):
            board[query[0]][i+1] = board[query[0]][i]
            small = min(small,board[query[0]][i])
        board[query[0]][query[1]+1] = tmp
        
        answer.append(small)
    return answer            
            
# Fuwari - 캡쳐 고정 프로그램 (Mac App Store)