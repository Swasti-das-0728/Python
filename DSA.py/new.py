# # def reverse_string(s):
# #     return s[::-1]

# # text = input("Enter a string: ")
# # print("Reversed string:", reverse_string(text))
# stack = []

# stack.append(10)
# stack.append(20)
# stack.append(30)

# print("Stack:", stack)

# stack.pop()

# print("After pop:", stack)


arr = [10, 45, 2, 99, 23]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest element:", largest)