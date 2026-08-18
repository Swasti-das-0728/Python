arr=[10,23,43,55,60]
target = int(input("ask a number to search"))
for i in range (len(arr)):
    if arr[i] == target:
        print(f"the array found at index",i)
        break
    else:
        print("-1")