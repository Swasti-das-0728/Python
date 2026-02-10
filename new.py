# import random

# number = random.randint(1, 100)
# attempts = 0

# print("🎮 Welcome to the Number Guessing Game!")
# print("Guess a number between 1 and 100")

# while True:
#     guess = int(input("Enter your guess: "))
#     attempts += 1

#     if guess < number:
#         print("Too low! Try again 🔽")
#     elif guess > number:
#         print("Too high! Try again 🔼")
#     else:
#         print(f"🎉 Correct! You guessed it in {attempts} attempts.")
#         break


# tasks = []

# while True:
#     task = input("Enter task (or 'exit' to stop): ")
#     if task == "exit":
#         break
#     tasks.append(task)

# print("\nYour To-Do List:")
# for t in tasks:
#     print("-", t)
import random

print("Rolling the dice...")
print("You got:", random.randint(1, 6))
