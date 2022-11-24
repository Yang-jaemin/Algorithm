def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3단계 
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4단계
    if answer[0] == '.':
        if len(new_id)>1:
            answer = answer[1:]
        else:
            answer = ''
            
    if answer[-1] == '.':
        if len(new_id)>1:
            answer = answer[:-1]
        else:
            answer = ''
    
    # 5단계
    if answer == '':
        answer = 'a'
        
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계
    while len(answer) < 3:
        answer += answer[-1]
    return answer