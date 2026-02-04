a = input("enter first number: ")
operator = input("enter operator (+,-,*,/,%) : ")
b = input("enter second number: ")

a = int(a)
b = int(b)

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
elif operator == "%":
    print(a % b)
else:
    print("invalid operation")
