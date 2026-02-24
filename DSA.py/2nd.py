from array import *
array1 = array('i', [3,4,5,6,7,7])
array1.pop(3)
array1.remove(3)
array1.insert(0,9)
for i in range(0,len(array1)):
    print(array1[i])
print(array1)