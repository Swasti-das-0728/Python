# the number divisible by other number
# num = int(input("enter a number"))
# result = {}

# for i in range (1,num//2):
#     if (num%i == 0):
#         result.append(i)
#     result.append(num)
# print(result)



num = int(input("Enter a number: "))
result = []

for i in range(1, num // 2 + 1):
    if num % i == 0:
        result.append(i)

result.append(num)
print(result)