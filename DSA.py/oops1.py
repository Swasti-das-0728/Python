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
class Bank:
    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance

b = Bank()
print(b.get_balance())