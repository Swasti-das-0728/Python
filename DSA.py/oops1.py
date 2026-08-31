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
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for animal in [Cat(), Dog()]:
    animal.sound()