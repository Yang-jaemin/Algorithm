def solution(numbers):
    newkey = [str(num) for num in numbers]
    
    newkey.sort(key = lambda x : x*3, reverse = True)
    # 1000이하니까 333이랑 303 이랑 뭐가 큰지 비교하면된다. 그래서 1의자리를 333으로 만들어야해서 *3
    
    return str(int(''.join(newkey)))  # [0,0,0,0] 나오면 0000인데 이건 0으로 출력해야하니까 int-> str