
# # # sentence = input("Enter a sentence: ")
# # # words = sentence.split()
# # # print("Total words:", len(words))



# # num = int(input("Enter a number: "))

# # if num % 2 == 0:
# #     print("Even number")
# # else:
# #     print("Odd number")


# import random
# import string

# length = int(input("Enter password length: "))

# characters = string.ascii_letters + string.digits + string.punctuation
# password = "".join(random.choice(characters) for _ in range(length))

# print("Generated Password:", password)

import time

seconds = int(input("Enter time in seconds: "))

while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1

print("Time's up! ⏰")
