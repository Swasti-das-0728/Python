# arr = [12, 11, 13, 5]

# for i in range(1, len(arr)):

#     key = arr[i]
#     j = i - 1

#     while j >= 0 and key < arr[j]:
#         arr[j + 1] = arr[j]
#         j -= 1

#     arr[j + 1] = key

# # print(arr)
# a = str(input("enter the string"))
# b = ""

# for i in range (len(a) -1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print(" paleindrom")
# else:
#     print("not")


number = float(input("enter the first num"))
number2 = float(input("enter the second num"))
sum = number + number2
print(sum)