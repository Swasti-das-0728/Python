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
# arr = [12, 45, 7, 89, 34]

# max_val = arr[0]

# for num in arr:
#     if num > max_val:
#         max_val = num

# print("Maximum:", max_val)
# arr = [5, 10, 15, 20]

# total = 0

# for num in arr:
#     total += num

# # print("Sum:", total)

# def binary_search(arr, key):
#     low = 0
#     high = len(arr)-1

#     while low <= high:
#         mid = (low+high)//2

#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# print(binary_search([10,20,30,40],30))

# arr = [5,3,8,4,2]

# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# # print(arr)
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# def binary_search(arr, key):
#     low = 0
#     high = len(arr)-1

#     while low <= high:
#         mid = (low+high)//2

#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# # print(binary_search([10,20,30,40],30))

# def binary_search(arr, key):
#     low = 0
#     high = len(arr)-1

#     while low <= high:
#         mid = (low+high)//2

#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# print(binary_search([10,20,30,40],30))
# n = int(input())


# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

# n = 1234

# sum = 0
# while n > 0:
#     sum += n % 10
#     n //= 10

# print(sum)

n = 1234

rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print(rev)