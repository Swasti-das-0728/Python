
# # # # # # sentence = input("Enter a sentence: ")
# # # # # # words = sentence.split()
# # # # # # print("Total words:", len(words))



# # # # # num = int(input("Enter a number: "))

# # # # # if num % 2 == 0:
# # # # #     print("Even number")
# # # # # else:
# # # # #     print("Odd number")


# # # # import random
# # # # import string

# # # # length = int(input("Enter password length: "))

# # # # characters = string.ascii_letters + string.digits + string.punctuation
# # # # password = "".join(random.choice(characters) for _ in range(length))

# # # # print("Generated Password:", password)

# # # import time

# # # seconds = int(input("Enter time in seconds: "))

# # # while seconds > 0:
# # #     print(seconds)
# # #     time.sleep(1)
# # #     seconds -= 1

# # # print("Time's up! ⏰")

# # age = 20
# # if age>20:
# #     print("you can marry anyone now")
# # elif age<18 and age>10:
# #     print("you are in teenage")
# # else:
# #     print("you are a mature")
# #     print(age)


# filename = input("Enter file name: ")

# with open(filename, "r") as file:
#     text = file.read()
#     words = text.split()

# print("Total Words:", len(words))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")
