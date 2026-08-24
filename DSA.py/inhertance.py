# class India:
#     cm = "narendraaaaa"
#     def budget(self):
#         print("200cr")
# class Odisha(India):
#     pass
# obj = Odisha()
# obj.budget()
# print( obj.cm )

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         original = x
#         reverse = 0

#         while x > 0:
#             digit = x % 10
#             reverse = reverse * 10 + digit
#             x = x // 10

#         return original == reverse


class Animal:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"hello name is {self.name}")
class Human(Animal):
    pass

person  = Human("Swasti")
person.show()
