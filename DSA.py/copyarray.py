from array import *
val = array('i', [10,20,30,40])



stealArray = array(val.typecode, (x for x in val))
for i in range(len(stealArray)):
    print(stealArray[i], end=" ")