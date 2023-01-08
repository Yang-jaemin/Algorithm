# 트리구조 탐색에는 DFS BFS가 있다!
# 트리 : 나무를 거꾸로 ( 부모 - 왼 - 오) 기본단위
# DFS(파고들어감 - 깊이우선탐색)
# 전위 순회 : 왼쪽 먼저 (부왼오)
# 중위순회 : (왼부오)
# 후위순회 : (왼오부)


# BFS : 넓이 우선 탐색이고 레벨별로 탐색
def DFS(x): # 전위순회(부왼오)
    if x>7:
        return
    else:
        print(x) 
        DFS(x*2) # 왼노드    
        DFS(x*2+1) # 오노드

def DFS(x): # 중위순회(왼부오)
    if x>7:
        return
    else:
        DFS(x*2) # 왼노드    
        print(x)
        DFS(x*2+1) # 오노드
    
def DFS(x): # 후위순회(왼오부) 병합정렬
    if x>7:
        return
    else:
        DFS(x*2) # 왼노드    
        DFS(x*2+1) # 오노드
        print(x) # 후위순회(왼오부)
            
if __name__ == "__main__":
    DFS(1)
