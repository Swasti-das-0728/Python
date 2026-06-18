# # armtrong number should be if 153 = 1*3 + 5*3 + 3*3 = 153
# n = 153
# num = n
# total = 0
# nod = len(str(n))
# while num>0:
#     ld = num % 10
#     total = total + (ld ** nod)
#     num = num // 10
# print ( total == n , "yes the number is armstrong number")



n = 23433
num = n
count = 0
while num>0:
    count+=1
    num = num // 10
print( count)