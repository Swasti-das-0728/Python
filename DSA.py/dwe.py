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


# class Candy:
#     def __init__(self,flavour,factory,rate):
#         self.flavour = flavour
#         self.factory = factory
#         self.rate = rate
#     def show(self):
#         print(f"the objects are {self.factory},{self.rate},{self.flavour}")
# pulse = Candy("chocolate",5,10)
# munch = Candy("strawberry",6,5)
# kitkat = Candy("pinapple",9,9)


# # question = str(input("enter your question"))
# # print(question)
# kitkat.show()
# class Birds:
#     name = "parrot"         
#     def __init__(self,color):
#         self.color = color

#     @classmethod
#     def hello(cls):
#         print("hello brother")
#     @staticmethod
#     def static():
#         print("hi")
# obj =  Birds("red")
# obj.hello()
# obj.static( )
        
class School:
    def __init__(self,rollno,domain,section):
        self.rollno = rollno
        self.name = domain
        self.section = section
    def sum(self,Firstnumber,Secondnumber):
        return Firstnumber * Secondnumber


Swasti = School(338,"Aiml",'b') 
tanmay = School(345,"st",'a')
priti = School(342,"cloud",'b')

result = Swasti.sum(34,22)
print(result)



print(Swasti.rollno)
print(tanmay.section)