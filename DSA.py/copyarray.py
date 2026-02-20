from array import *
val = array('i', [10,20,30,40])

# to copy the array 

# stealArray = array(val.typecode, (x for x in val))
# for i in range(len(stealArray)):
#     print(stealArray[i], end=" ")



# to delete the array
stealArray.pop(2)

stealArray = array(val.typecode, (x for x in val))
for i in range(len(stealArray)):
    print(stealArray[i], end=" ")
