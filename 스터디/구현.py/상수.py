# a,b = map(str,input().split())
# a = list(a)
# print(a)
# # a = a[::-1]
# # b = b[::-1] # 뒤집는 과정 구현해보기
# for i in range(len(a)//2):
#     a[i], a[len(a)-1-i] =  a[len(a)-1-i], a[i]
# print(int("".join(a)))
    
    
# if int(a)>int(b):
#     print(a)
# else:
#     print(b)

# 그냥 문자열로( 왜안댐?)
# a,b = map(str,input().split())
# for i in range(len(a)//2):
#     a[i], a[len(a)-1-i] = a[len(a-1-i)], a[i]
# for i in range(len(b)//2):
#     b[i], b[len(b)-1-i] = b[len(b-1-i)], b[i]
# print(max(int(a),int(b)))

# 리스트로
# a,b = map(str,input().split())
# a = list(a)
# b = list(b)
# A =''
# B =''
# for i in range(len(a)//2):
#     a[i], a[len(a)-1-i] = a[len(a-1-i)], a[i]
# for i in range(len(b)//2):
#     b[i], b[len(b)-1-i] = b[len(b-1-i)], b[i]
# print(a)
# A = int("".join(a))
# B = int(''.join(b))
# print(max(A,B))
a,b =map(str,input().split())
new_a = ''
new_b = ''
for c in a:
    new_a = c + new_a
for d in b:
    new_b = d + new_b
print(max(int(new_a),int(new_b)))
    

     