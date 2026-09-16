from abc import ABC , abstractmethod
class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass
    

class Square:
    def __init__(self,side):
        self.side = side
class Circle:
    def __init__(self,radius):
        self.radius= radius
    def perimeter(self):
        print("hello")
    def area(self):
        print("hlowwww")


obj = Circle(3)
