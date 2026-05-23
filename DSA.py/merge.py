# # # # arr = [5, 1, 4, 2]

# # # # n = len(arr)

# # # # for i in range(n):
# # # #     for j in range(0, n-i-1):

# # # #         if arr[j] > arr[j+1]:
# # # #             arr[j], arr[j+1] = arr[j+1], arr[j]

# # # # print(arr)
# # # arr = [64, 25, 12, 22]

# # # for i in range(len(arr)):

# # #     min_index = i

# # #     for j in range(i+1, len(arr)):
# # #         if arr[j] < arr[min_index]:
# # #             min_index = j

# # #     arr[i], arr[min_index] = arr[min_index], arr[i]

# # # print(arr)
# # def merge_sort(arr):

# #     if len(arr) > 1:

# #         mid = len(arr)//2

# #         left = arr[:mid]
# #         right = arr[mid:]

# #         merge_sort(left)
# #         merge_sort(right)

# #         i = j = k = 0

# #         while i < len(left) and j < len(right):

# #             if left[i] < right[j]:
# #                 arr[k] = left[i]
# #                 i += 1
# #             else:
# #                 arr[k] = right[j]
# #                 j += 1

# #             k += 1

# #         while i < len(left):
# #             arr[k] = left[i]
# #             i += 1
# #             k += 1

# #         while j < len(right):
# #             arr[k] = right[j]
# #             j += 1
# #             k += 1

# # arr = [38, 27, 43, 3]

# # merge_sort(arr)

# # print(arr)
# arr = [
#     [1, 2],
#     [3, 4]
# ]

# # for row in arr:
# #     print(row)
# def bubble(arr1):
#     n = len(arr1)
#     for i in range(n):
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr1[j] > arr1[j+1]:
#                 arr1[j] , arr1[j+1] = arr1[j+1], arr1[j]
#                 swapped = True
#                 if not swapped:
#                     break
#     return arr1

# arr1 = [23,45,43,12]
# bubble(arr1)
# print("sorted:", arr1)
# /selection sort

def selection(arr1):
    n = len(arr1)
    for i in range(n-1):
        mini = i
        for j in range (i+1 , n):
            if(arr1[j]<arr1[mini]):
                mini = j
        arr1[i],arr1[mini] = arr1[mini],arr1[i]
arr1 = [32,44,11,54,29]
selection(arr1)
print("sorted array are :", arr1)