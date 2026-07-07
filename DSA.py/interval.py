# # a = 10
# # b = 22
# print(a*b)
# print(a%b)
# print(a^b)
# print(a-b)
# print(a+b)
# print(a/b)
# print( 343 ==  234 and 34>43)

# job = int(input("please give me the cgpa :- "))
# if job == 7:
#     print("i will accept the job")
# else:
#     print("i don't need this")

# money = int(input("enter the money :-"))
# if money == 21:
#     print("hat")
# else:
#     print("no")
# # str1 = str(input("enter a string"))
# # str2 = str(input("enter a string"))
# # if len(str1) > len(str2):
# #     print("str1 is greater one")
# # else:
# #     print("last one is bigger") 
# # position = input("please tell me your roll in a game")
# # if position == 'rusher':
# #     print("practice atleast 5hr")
# # else:
# #     print("go with the flow")

# # num = int(input("provide your number"))
# # if num % 2 == 0 :
# #     print("it is a even number")
# # else:
# # #     print("odd")
# # name = input("enter your name")
# # age = int(input("enter the age"))

# # if age> 18:
# #     print("hello + {name} you are a valid voter")
# # else:
# #     print("wait till 18")

# # num = int(input("enter the table number"))
# # for i in range(num,(num*10+1),num):
# #     print(i)
# # a = "swasti"
# # for i in range(len(a)):
# #     print(a[i])
# # a = "teg thryuy erdfuf"
# # for i in  a:
# #     if i == 'y':
# #         break
# #     else:
# #         print(i)

# # def second_largest(arr):

# #     first = second = float('-inf')

# #     for num in arr:

# #         if num > first:
# #             second = first
# #             first = num

# #         elif num > second and num != first:
# #             second = num

# #     return second


# # arr = list(map(int, input("Enter array: ").split()))

# # print(second_largest(arr))
# def pair_sum(arr, target):

#     seen = set()

#     for num in arr:

#         if target - num in seen:
#             return True

#         seen.add(num)

#     return False


# arr = list(map(int, input().split()))

# target = int(input("Target: "))

# # print(pair_sum(arr, target))
# def frequency(arr):

#     freq = {}

# #     for i in arr:

# #         if i in freq:
# #             freq[i] += 1
# #         else:
# #             freq[i] = 1

# #     return freq


# # arr = list(map(int, input().split()))

# # print(frequency(arr))
# print("Hello World")

# name = input("Enter your name: ")
# print("Welcome", name)

# number = int(input("enter the digit"))
# for i in range(number):
#     if(i<number):
#         print("hello world")
#     else:
#         print("no words")
# # n = int(input("enter an number"))
# # for i in range(0,n+1,1):
# #     print(i)
# n = int(input("enter an number"))
# for i in range(n,0,-1):
# #     print(i)
# n = int(input("enter an number"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")
# n = int(input("enter a number"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(f"your factorial is {fact}")
n = int(input("enter a number"))
even = 0
odd = 0
for i in range(1,n+1):
    if i%2 == 0:
        even = even+ i
    else:
        odd = odd + i
print(f"your even and odd are {even},{odd}")


