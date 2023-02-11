from collections import deque
def solution(routes):
    routes.sort(key = lambda x : (x[1]))
    print(routes)
    routes = deque(routes)
    cnt = 1
    camera = routes[0][1]
    routes.popleft()
    for route in routes:
        if camera < route[0]:
            cnt += 1
            camera = route[1]
    return cnt
            