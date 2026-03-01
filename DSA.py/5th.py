# # def reverse_string(s):
# #     return s[::-1]

# # print(reverse_string("swasti"))

# def binary_search(arr, target):
#     left, right = 0, len(arr)-1
    
#     while left <= right:
#         mid = (left + right) // 2
        
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# print(binary_search([1,2,3,4,5], 4))
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()