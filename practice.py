nums = [1,2,3,4]
cnt = 0
rcnt = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            a = nums[i]+nums[j]+nums[k]
            print(a)
            # for i in range(2,a+1):
            #     if a%i == 0:
            #         cnt+=1
            # else:
            #     if cnt == 1:
            #         rcnt +=1
            #         cnt = 0
        
                
