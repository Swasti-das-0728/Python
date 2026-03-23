# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # Insert at end
#     def insert(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         temp = self.head
#         while temp.next:
#             temp = temp.next

# # #         temp.next = new_node

# # #     # Display list
# # #     def display(self):
# # #         temp = self.head
# # #         while temp:
# # #             print(temp.data, end=" -> ")
# # #             temp = temp.next
# # #         print("None")


# # # # Create Linked List
# # # ll = LinkedList()

# # # ll.insert(10)
# # # ll.insert(20)
# # # ll.insert(30)

# # # ll.display()

# # def findSum(a, b):
# #     i, j = len(a) - 1, len(b) - 1
# #     carry = 0
# #     result = []

# #     while i >= 0 or j >= 0 or carry:
# #         sum_val = carry

# #         if i >= 0:
# #             sum_val += int(a[i])
# #             i -= 1
# #         if j >= 0:
# #             sum_val += int(b[j])
# #             j -= 1

# #         result.append(str(sum_val % 10))
# #         carry = sum_val // 10

# #     return ''.join(result[::-1])
# # arr = [5,3,8,4,2]

# # for i in range(len(arr)):
# #     for j in range(len(arr)-i-1):
# #         if arr[j] > arr[j+1]:
# #             arr[j], arr[j+1] = arr[j+1], arr[j]

# # printkhn(arr);

# # def binary_search(arr, target):
# #     left = 0
# #     right = len(arr) - 1

# #     while left <= right:
# #         mid = (left + right) // 2

# #         if arr[mid] == target:
# #             return mid
# #         elif arr[mid] < target:
# #             left = mid + 1
# #         else:
# #             right = mid - 1

# #     return -1


# # # Example
# # arr = [1, 3, 5, 7, 9, 11]
# # target = 7

# # result = binary_search(arr, target

# # if result != -1:
# #     print("Element found at index:", result)
# # else:
# #     print("Element not found")

# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None


# # class LinkedList:
# #     def __init__(self):
# #         self.head = None

# #     # Insert at end
# #     def insert(self, data):
# #         new_node = Node(data)

# #         if self.head is None:
# #             self.head = new_node
# #             return

# #         temp = self.head
# #         while temp.next:
# #             temp = temp.next

# #         temp.next = new_node

# #     # Display list
# #     def display(self):
# #         temp = self.head
# #         while temp:
# #             print(temp.data, end=" -> ")
# #             temp = temp.next
# #         print("None")


# # # Create Linked List
# # ll = LinkedList()

# # ll.insert(10)
# # ll.insert(20)
# # ll.insert(30)

# # ll.display()

# # n = int(input())

# # if n % 2 == 0:
# #     print("Even")
# # else:
# #     print("Odd")

# a = 5
# b = 10

# a, b = b, a

# # print(a, b)

# n = int(input())

# a, b = 0, 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
