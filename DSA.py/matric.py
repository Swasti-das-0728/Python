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
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

obj = B()
obj.show()