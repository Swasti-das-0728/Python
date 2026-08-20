# arr=[10,23,43,55,60]
# target = int(input("ask a number to search"))
# for i in range (len(arr)):
#     if arr[i] == target:
#         print(f"the array found at index",i)
#         break
#     else:
#         print("-1")

# x = [1,2,3]
# y = x
# y.append(4)
# print(x)
# class Swasti:
#     a = "hari"
#     def sum(self):

#         print("add two number")
# obj = Swasti()
# obj.sum()
# print(obj.a)


# Constructor


class Candy:
    def __init__(self,flavour,factory,rate):
        self.flavour = flavour
        self.factory = factory
        self.rate = rate
pulse = Candy("chocolate",5,10)
munch = Candy("strawberry",6,5)
kitkat = Candy("pinapple",9,9)

# question = str(input("enter your question"))
# print(question)
print(kitkat.factory)