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

# # print(D.mro())
# # class Bank:
# #     def __init__(self):
# #         self.__balance = 1000

# #     def get_balance(self):
# #         return self.__balance

# # b = Bank()
# # print(b.get_balance())

# # class Parent:
# #     def __init__(self):
# #         print("Parent")

# # class Child(Parent):
# #     pass

# # # Child()

# # class Student:
# #     college = "MIT"

# #     def __init__(self, name):
# #         self.name = name

# # s1 = Student("Alice")
# # s2 = Student("Bob")

# # Student.college = "Harvard"

# # print(s1.college)
# # print(s2.college)

# n = 5
# s = "1"

# for _ in range(n - 1):
#     ans = ""
#     count = 1

#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             ans += str(count) + s[i - 1]
#             count = 1

#     ans += str(count) + s[-1]
#     s = ans

# print(s)


# from itertools import groupby

# class Solution:
#     def countAndSay(self, n: int) -> str:
#         s = "1"

#         for _ in range(n - 1):
#             s = "".join(str(len(list(g))) + k for k, g in groupby(s))

#         return s
class Solution:
    def countAndSay(self, n: int) -> str:
        curr = "1"

        for _ in range(1, n):
            left = 0
            nxt = ""

            for right in range(len(curr)):
                if curr[right] != curr[left]:
                    nxt += str(right - left) + curr[left]
                    left = right

            nxt += str(len(curr) - left) + curr[left]
            curr = nxt

        return curr