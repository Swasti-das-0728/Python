def selection(arr1):
    n = len(arr1)

    for i in range(n-1):
        mini = i

        for j in range(i+1, n):

            if(arr1[j] < arr1[mini]):
                mini = j

        arr1[i], arr1[mini] = arr1[mini], arr1[i]

arr1 = [32,44,11,54,29]

selection(arr1)

print("sorted array are :", arr1)