n = [2,4,3,3,2,6,5,7,9]
m = [5,2,9,7,1,3,2,9,8]
hash_list = [0]*10
for num in n:
    hash_list[num]+=1
for num in m:
    if num<1 or num>10:
        print("0")
    else:
        print(hash_list[num])
