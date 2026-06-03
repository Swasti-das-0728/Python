# arr = [1, 2, 3, 4, 5]

# even = 0
# odd = 0

# for i in arr:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even:", even)
# print("Odd:", odd)
arr = [1, 2, 3, 4]

first = arr[0]

for i in range(len(arr)-1):
    arr[i] = arr[i+1]

arr[-1] = first

print(arr)