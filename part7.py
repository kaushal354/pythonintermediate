#write a function to calculate the area of a circle given a radius.
import numpy as np
def areaOfcircle(r):
    area = np.pi * (r **2)
    print(round(area,2))
    return round(area,2)

areaOfcircle(9)
areaOfcircle(5)


#Create a function to check if a number is prime.
def primenum_check(a):
    b = 0
    for i in range(1,a+1):
        if a % i == 0:
            b = b + 1
        else:
            b = b + 0
    if b == 2:
        return "it is a prime"
    else:
        return "it is not a prime"

for i in range(1,12):
    print(i,":",primenum_check(i))



#Implement a function that reverses a given string.
def revstring(a):
    for i in range(0,len(a)):
        print(a[3-i],end = "")

revstring("hello")


# Given a list of numbers, create a function to find the sum
# of all positive numbers
def positivenum(list):
    a = 0
    for i in range(0,len(list) - 1):
        if list[i] > 0:
            a = a + list[i]
        else:
            a = a + 0
    return a

list = [1,2,3,4,5,6,-2,-9,-22,-3]
print(positivenum(list))





#Write a Python function to check if a given string is a
#palindrome
def palindrome(str):
    str2 = str
    loop = int((len(str) - 1) / 2)
    j = 0
    for i in range(0,loop):
        if str[i] == str2[(len(str) - 1) - i]:
            j = j + 1
        else:
            j = j + 0
    if j == loop:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")

str = "itopinonavevanonipoti"
palindrome(str)



# Implement a function that returns the factorial of a given
# number using recursion.
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(5))


#creaate a function to find the square of each element in a given list

def squareel(list1):
    dict1 = {}
    a = 0
    for i in range(0,len(list1)):
         a = (list1[i])**2
         dict1.update({list1[i] : a})
    return dict1

list1 = [1,2,3,4,5,6,7,8,9]
print(squareel(list1))

#write a function to check if a number is even or odd and return "even"
#or "odd" accordingly
def evnorodd(n):
    if n % 2 ==0:
        return "even"
    else:
        return "odd"

n = int(input("enter a given numbers:-"))
print(evnorodd(n))

#calculate the area of a traingle given its base and height using a function
def areatri(b,h):
    a = 0.5 *(b*h)
    return a

b = int(input("enter a base of triangle:"))
h = int(input("enter a height of triangle:"))
print(areatri(b,h))

#write a function that takes two lists and returns their intersection
#(common elements).
def intersectionoflst(list1,list2):
    a = set(list1).intersection(set(list2))
    return a

#taking input by split method
list1 = []
list1 = list(input("Enter multiple values: ").split())
list2 = []
list2 = list(input("Enter multiple values: ").split())
print(intersectionoflst(list1,list2))

#taking input by loop method
a = int(input("how many element you want to enter for list1?"))
list1 = []
for i in range(a):
    num = int(input("enter a number element for list 1:"))
    list1.append(num)
    i += 1
b = int(input("how many element you want to enter for list2?"))
list2 = []
for j in range(b):
    num = int(input("enter a number element for list 2:"))
    list2.append(num)
    j += 1
print(intersectionoflst(list1,list2))




#implement a function to check if a given year is a leap year or not
def leapyear(n):
    if n % 400 == 0:
        return "it is a leap year"
    elif n % 100 == 0:
        return "it is not a leap year"
    elif n % 4 == 0:
        return "it is a leap year"
    else:
        return "it is not a leap year"

n = int(input("enter a year:"))
print(leapyear(n))




#create a function that takes a number as input and prints its multiplication table
def multiplicationtable(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
        i += 1

n = int(input("enter a number which multiplication table you want to print:-"))
multiplicationtable(n)


