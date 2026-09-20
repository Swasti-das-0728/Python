def decorate(func):
    def wrapper():
        print("i am swasti")
        func()
        print("i am deepan")
    return wrapper

@decorate
def hello():
    print("hello i am das")

hello()
