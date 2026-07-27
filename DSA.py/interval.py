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
# n = int(input("enter a number"))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even+ i
#     else:
#         odd = odd + i
# print(f"your even and odd are {even},{odd}")

# n = int(input("Enter a number: "))

# even = 0
# odd = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i

# print("Sum of even numbers =", even)
# print("Sum of odd numbers =", odd)

# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(f"the factor is {fact}")
# n = int(input("Enter a number: "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even+i
#     else:
#         odd = odd+i
# print(even , odd)
# n = int(input("Enter a number: "))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)
        
# n = int(input("Enter a number: "))
# sum =0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i
# if sum == n:
#     print("it is a perfect number")
# print(sum)
        
       
# n = int(input("Enter a number: "))
# prime=0
# for i in range(1,n+1):
#     if n%i == 0:
#         prime = prime + 1
# print(prime)
# if prime<=2:
#     print("this is a prime number")
         

# a = "swasti"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print("it is a pallendrom")
# else:
#     print("not paliendrom")
# n = int(input("enter a number"))

# a = "katak"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print("it is a paleindrom")
# else:
#     print("not a paleindrom")
# n = int(input("enter a number"))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count = count + 1
#         print(f"the prime of this number are{count}")
# if count <= 2:
#     print("this is a prime number")
# else:
#     print("this is not a prime number")
# a = "dshfi454@&$^^dfh"
# char = 0
# dig = 0
# spchr = 0
# for i in a:
#     if i.isdigit():
#         dig = dig+1
#     elif i.isalpha():
#         char = char+1
#     else:
#         spchr = spchr+1
# print(f"your digit are {dig}\n your alphabets are {char}\n your special character are{spchr}")

# # n = int(input("enter a number"))
# a = int(input("enter a number"))
# while a>0:
#     print(a%10)
#     a = a//10
# n = int(input("enter a number"))
# rev=0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n//10
# print(rev)

# a = int(input("enter an number"))
# rev = 0
# copy = a
# while a>0:
#     rev = rev*10 + a% 10
#     a = a//10
# if copy == rev:
#     print("pallendromic number")
# else:
#     print("not similar")


# import random

# num = random.randint(1, 11)
# tries = 0

# while True:
#     guess = int(input("Guess your number: "))
#     tries += 1

#     if num == guess:
#         print("You are correct!")
#         print("Tries:", tries)
#         break

#     elif num > guess:
#         print("Try higher")

#     else:
#         print("Try lower")

# functions
# # there is different type of functions like int len etc..
# def mul(a,b):
#     print(f"the sum is {a*b}")
# mul(3,88)
# mul(3,28)
# # mul(3,8)
# def intro(name,age=22):
#     print(f"your name is{name} and age{age}")
# intro( "swasti",32)
# def pallendrome(str):
#     rev = ""
#     for i in range(len(str)-1,-1,-1):
#         rev = rev + str[i]
#     if rev==str:
#         print("this string is a pallendrom")
#     else:
#         print("it is not a pallendrom")
# pallendrome("navan")
# a =[12,43,66,32]     
# a.append(21)
# a.remove(66)
# a.remove(12)
# print(a)

# n = [23,6,-32,-53,9]
# for i in n:
#     if i  >=0:
#         print(f"positive number {i}")

# for i in n:
#     if i<0:
#         print(f"negative are{i}")
# n = [2,4,3555,2,4,2]
# sum = 0
# for i in n:
#     sum = sum + i
# print(sum/len(n))
    
# n = [2,34,54,33,87]
# largest = n[0]
# index = 0
# for i in range(len(n)):
#     if n[i] > largest:
#         largest == n[i]
#         index = i
# print(n[i])
# def max_index(arr):

#     max_idx = 0

#     for i in range(1, len(arr)):

#         if arr[i] > arr[max_idx]:
#             max_idx = i

#     return max_idx


# arr = list(map(int, input("Enter array: ").split()))

# print("Maximum Index =", max_index(arr))
# print("Maximum Value =", arr[max_index(arr)])
# print("cockroach" "Janta" "Party")
a = int(input("enter a number"))
try:
    print(a/10)
except Exception as err:
    print("you can't multiply 0")
print("printing done")