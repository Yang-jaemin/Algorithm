num = [1,2,3] # 몇개인지 알고있으니까 for 문 되긴하는데 모르면?
a = []
for i in range(len(num)):
    for j in range(len(num)):
        for k in range(len(num)):
            print(num[i],num[j],num[k])

    
    