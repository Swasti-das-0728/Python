#  this is used to take array import array

from array import *

val = array('i', [10,20,30,40])
print(val)
for i in range(0,4):
    print(val[i] , end=" ")

print('\n')

for x in val:
    print(x , end=" ")

print("\n")
    # for typecode
print(val.typecode)

val.reverse()
for x in val:
    print(x , end=" ")
print("\n")

val.insert(3, 233)
val.append(434)
val[1] = 43434

for x in val:
    print(x , end=" ")