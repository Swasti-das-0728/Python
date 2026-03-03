# # # # def reverse_string(s):
# # # #     return s[::-1]

# # # # print(reverse_string("swasti"))

# # # def binary_search(arr, target):
# # #     left, right = 0, len(arr)-1
    
# # #     while left <= right:
# # #         mid = (left + right) // 2
        
# # #         if arr[mid] == target:
# # #             return mid
# # #         elif arr[mid] < target:
# # #             left = mid + 1
# # #         else:
# # #             right = mid - 1
# # #     return -1

# # # print(binary_search([1,2,3,4,5], 4))
# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None

# # class LinkedList:
# #     def __init__(self):
# #         self.head = None

# #     def insert(self, data):
# #         new_node = Node(data)
# #         if not self.head:
# #             self.head = new_node
# #             return
        
# #         temp = self.head
# #         while temp.next:
# #             temp = temp.next
# #         temp.next = new_node

# #     def display(self):
# #         temp = self.head
# #         while temp:
# #             print(temp.data, end=" -> ")
# #             temp = temp.next

# # ll = LinkedList()
# # ll.insert(10)
# # ll.insert(20)
# # ll.insert(30)
# # ll.display()

# def max_subarray_sum(arr, k):
#     window_sum = sum(arr[:k])
#     max_sum = window_sum
    
#     for i in range(k, len(arr)):
#         window_sum += arr[i] - arr[i-k]
#         max_sum = max(max_sum, window_sum)
    
#     return max_sum

# print(max_subarray_sum([2,1,5,1,3,2], 3))
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

print(lcs("abcde", "ace"))