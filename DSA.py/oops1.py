# class A:
#     def show(self):
#         print("A")

# class B(A):
#     pass

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):
#     pass

# d = D()
# d.show()

# print(D.mro())
# class Bank:
#     def __init__(self):
#         self.__balance = 1000

#     def get_balance(self):
#         return self.__balance

# b = Bank()
# print(b.get_balance())

# class Parent:
#     def __init__(self):
#         print("Parent")

# class Child(Parent):
#     pass

# Child()

class Student:
    college = "MIT"

    def __init__(self, name):
        self.name = name

s1 = Student("Alice")
s2 = Student("Bob")

Student.college = "Harvard"

print(s1.college)
print(s2.college)