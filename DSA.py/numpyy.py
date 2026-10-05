# class Dog:
#     def sound(self):
#         print("Dog says: Woof")


# class Cat:
#     def sound(self):
#         print("Cat says: Meow")


# dog = Dog()
# cat = Cat()

# dog.sound()
# cat.sound()
class Dog:
    def sound(self):
        print("Woof")


class Cat:
    def sound(self):
        print("Meow")


def animal_sound(animal):
    animal.sound()


animal_sound(Dog())
animal_sound(Cat())