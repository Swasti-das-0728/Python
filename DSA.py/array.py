from array import *
hid = array('i', [1,2,3,4,5,6,7,8,9,10,11])

a = hid[2: 5]
print("\n")
# print(hid[2])
# copyArray = array(hid.typecode, (x for x in hid))
for x in range(len(a)):
    print(a[x])


