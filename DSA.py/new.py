# # # # # def reverse_string(s):
# # # # #     return s[::-1]

# # # # # text = input("Enter a string: ")
# # # # # print("Reversed string:", reverse_string(text))
# # # # stack = []

# # # # stack.append(10)
# # # # stack.append(20)
# # # # stack.append(30)

# # # # print("Stack:", stack)

# # # # stack.pop()

# # # # print("After pop:", stack)


# # # # arr = [10, 45, 2, 99, 23]

# # # # largest = arr[0]

# # # # for num in arr:
# # # #     if num > largest:
# # # #         largest = num

# # # # print("Largest element:", largest)from collections import deque
# # # from collections import deque

# # # queue = deque()

# # # queue.append(10)
# # # queue.append(20)
# # # queue.append(30)

# # # print("Queue:", queue)

# # # queue.popleft()

# # # print("After dequeue:", queue)
# # def fibonacci(n):
# #     a, b = 0, 1

# #     for i in range(n):
# #         print(a, end=" ")
# #         a, b = b, a + b

# # n = int(input("Enter number: "))

# # fibonacci(n);

# # arr = [10, 5, 20, 8, 25]

# # largest = second = -9999

# # for num in arr:
# #     if num > largest:
# #         second = largest
# #         largest = num
# #     elif num > second and num != largest:
# #         second = num

# # print("Second largest:", second)
# arr = [1,2,2,3,3,3,4]

# freq = {}

# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# print(freq)
arr = [12, 45, 7, 89, 34]

max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num

print("Maximum:", max_val)