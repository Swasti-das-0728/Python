# class Solution:
#     def countAndSay(self, n: int) -> str:
#         s = "1"

#         for _ in range(n - 1):
#             ans = ""
#             i = 0

#             while i < len(s):
#                 count = 1

#                 while i < len(s) - 1 and s[i] == s[i + 1]:
#                     count += 1
#                     i += 1

#                 ans += str(count)
#                 ans += s[i]
#                 i += 1

#             s = ans

# #         return s
# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# class Cow:
#     def sound(self):
#         print("Moo")

# animals = [Dog(), Cat(), Cow()]

# for animal in animals:
#     animal.sound()
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# obj = B()
# # obj.show()
# class Student:
#     college = "CUTM"

# s1 = Student()
# s2 = Student()

# print(s1.college)
# print(s2.college)
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show(self):
        print(self.balance)

b = Bank(1000)
b.deposit(500)
b.show()