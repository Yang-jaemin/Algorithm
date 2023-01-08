n = int(input())
IDS = []
check = set()
j = -1
cc = ''
bb = True
for _ in range(n):
    ID = input()
    IDS.append(ID)
    
while bb:
    for i in range(len(IDS)):
        check.add(IDS[i][j:])
    if len(check) != len(IDS):
        j -= 1
        check = set()
    else:
        print(-j)
        bb =  False

    
    






















# n=int(input())
# nums=[]
# for _ in range(n):
#     nums.append(str(input()))
# for i in range(1, len(nums[0])+1):
#     results=[]
#     for j in range(n):
#         if nums[j][-i:] in results:
#             break
#         else:
#             results.append(nums[j][-i:])
#     if len(results)==n:
#         print(i)
#         break