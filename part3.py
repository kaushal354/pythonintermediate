# #write a program that checks if a given no is 
# #positive, negative or zeros
# num = int(input("enter a number:"))
# if num > 0:
#     print("it is positive no")
# elif num == 0:
#     print("it is zeros")
# else:
#     print("it is negative no")

# #create a loop that prints the first 10 even number
# for i in range(0,11,2):
#     print(i)

# #implement a program that finds the largest number
# #in list
# list1 = [2,5,3,9,5]
# list1.sort()
# print(list1[len(list1) - 1])

# #create a program that takes a year as input and
# #checks if it is a leap year or not
# year = int(input("enter a year:"))
# if year % 400 == 0:
#     print("it is leap year")
# elif year % 100 == 0:
#     print("it is not leap year")
# elif year % 4 == 0:
#     print("it is leap year")
# else:
#     print("it is not a leap year")

# #given a list of integers, find all the even numbers
# #and store them in a new list
# list4 = [1,3,5,7,9,2,6,4,8,6,12]
# even = []
# for i in range(0,len(list4)):
#     if list4[i] % 2 == 0:
#         even.append(list4[i])
#         print(list4[i])
# print("even:",even)

# #write a python program to check if a given no is 
# #prime number
# num2 = int(input("enter a number:"))
# j = 0
# for i in range(1,num2+1):
#     if num2 % i == 0:
#         j = j + 1
#     else:
#         j = j + 0
# if j == 2:
#     print("it is prime no")
# else:
#     print("it is not a prime no")

# #create a program that generates the fibonacci
# #sequence to a given number of terms
# series = int(input("enter a number:"))
# i = 0
# j = 1
# print(i,end = " ")
# print(i+j,end = " ")
# for num in range(0,series - 2):
#     a = j + i
#     if i < j:
#         i = a
#         print(i,end = " ")
#     else:
#         j = a
#         print(j,end = " ")

# #given a list of names, print all names starting
# #with the letter 'A'.
# list2 = ["Aditya", "Abhishek" ,"Komal", "Aryan", "Kaushal"]
# for i in range(0,len(list2)):
#     a = str(list2[i])
#     if a[0] == "A":
#         print(a)
#     elif a[0] == "a":
#         print(a)
#     else:
#         pass

# #implement a program that prints the multiplication
# #table of given no
# num6 = int(input("enter a no:"))
# for i in range(1,11):
#     mul = num6 * i
#     print(num6 ,"x", i, "=", mul )

# #program that calculates the factorial of a given
# #number
# num36 = int(input("enter a number: "))
# fact = num36
# for i in range(1,num36):
#     fact = fact * (num36-1)
#     num36 -= 1

# print(fact)

# #create a loop that prints all prime no between
# #1 and 50.
# a = 0
# for i in range(1,51):
#     for j in range(1,i+1):
#         if i % j == 0:
#             a = a + 1
#         else:
#             a = a + 0
#     if a == 2:
#         print(i,end = " ")
#     elif a < 2 and a > 2:
#         pass
#     a = 0

# #given a list of words, count the number of words
# #with more than five characters
# list9 = ["hello","kaushal","we","happy","kamesar"]
# a = 0
# for i in range(0,len(list9)):
#     l =  len(str(list9[i]))
#     if l > 5:
#         a = a + 1
#     else:
#         a = a + 0
# print(a)

#calculate the sum of digits of a given no
num19 = int(input("enter a number: "))
a = 0
if num19 >= 10:
    while num19 >= 10:
        c = num19 % 10
        a = a + c
        num19 = num19 // 10
        if num19 < 10:
            b = num19 + a
            print(b)
else:
    print(num19)









