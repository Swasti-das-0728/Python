class Factory:
    __a = "Bandra"
    def show(self):
        print(Factory.__a)
obj = Factory()
obj.show()
# obj = Factory()
# class Hello(Factory):
#     def show2(self):
#         print(super().a)
# obj = Hello()
# obj.show2()
