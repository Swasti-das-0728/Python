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


# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(f"hello name is {self.name},")
# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
#     def show(self):
#         print(f"hello name is {self.name},{self.age}")
#     pass

# animal = Animal("lion")
# person = Human("swasti",82)

# person.show()

# class School:
#     def __init__(self,name):
#         self.name = name
        
#         print(f"hello there {self.name}")

    

# class Tuition:
#     def __init__(self,name,address):
#         self.name = name
#         self.address = address
#         print(f"hello there name is {self.name},{self.address}")
# class Teacher(Tuition,School):
#     pass

# sdd = School("swasti",34)

# School.show()
    

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for _ in range(n - 1):
            i = 0
            ans = ""

            while i < len(s):
                count = 1

                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1

                ans += str(count) + s[i]
                i += 1

            s = ans

        return s