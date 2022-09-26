arr = [5,3,7,9,2,5,2,6]

arrMin = float('inf')
for i in range(len(arr)): # len(arr) = 8 , 0~7 index 번호
   if arr[i] < arrMin:    # 뒤의 것으로 바꾸라고 한다면 =를 넣어주어서 뒤에 값으로 바꿀 수 있음
       arr[i] = arrMin
    
print(arrMin)

# 이렇게도 가능

arrMin = arr[0]             # 처음 값으로 초기화
for i in range(1,len(arr)): # 0~7이 아니라 1~7으로 바뀜
   if arr[i] < arrMin:      # 뒤의 것으로 바꾸라고 한다면 =를 넣어주어서 뒤에 값으로 바꿀 수 있음
       arr[i] = arrMin
    
print(arrMin)

# 이렇게도 가능

arrMin = float('inf')
for x in arr:        # 배열의 값이 x로 바로 들어감
   if x < arrMin:    # 뒤의 것으로 바꾸라고 한다면 =를 넣어주어서 뒤에 값으로 바꿀 수 있음
       x = arrMin
    
print(arrMin)

