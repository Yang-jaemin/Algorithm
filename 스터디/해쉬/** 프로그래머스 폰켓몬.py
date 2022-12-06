def solution(nums): # 200ms
    pick = len(nums)//2
    answer = []
    for x in nums:
        if x not in answer:
            answer.append(x)
            if len(answer) == pick:
                break

    return len(answer)
# 해쉬 안쓰고 했음

# nums=[1,1,3,2,1,2]
def solution(nums): # 1ms
    #d = set(nums)
    d = set()
    for x in nums: 
        d.add(x)
    # d = (1,2,3)
    return min(len(d), len(nums) // 2)
# len(nums) // 2 