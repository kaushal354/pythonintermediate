#variables and data types
#create variable for storing a person's name, age, and  avg test score
name = input("enter a name:")
age = int(input("enter a age:"))
avgtestscore = int(input("enter a avgtestscore:"))

#concatenate two strings and print the result.
str1 = "hello"
str2 = "world"
string = str1 + " " +  str2
print(string)

#create a list of fruits and access element
# using indexing
list1 = ["apple","mango","banana"]
print(list1[0])
print(list1[1])
print(list1[2])

#given a list of numbers, find the sum and avg.
num = [1,2,3,4,5,6]
lenth = len(num)
num1 = 0
for i in range(0,lenth):
    num1 = num1 + num[i]

print(num1)
avg = num1 / lenth
print(avg)

#create a program that takes a temp in celsius and
# convert it to kelvin
celsius = int(input("enter a temp in celcius:"))
kel = celsius + 273
print("kelvin:",kel)

#implement a program that checks if a given string is
#palindrome
string2 = input("enter a string:")
lengof = len(string2) - 1
loop = lengof / 2
no = int(loop)
string = string2
j = 0
for i in range(0,no):
    if string[i] == string[lengof - i]:
        j = j + 1
    else:
        j = j + 0
if j == no:
    print("it is palindrome")
else:
    print("it is not a palindrome")

#function to reverse a given string.
def reversestr():
    str3 = input("enter a string:")
    length3 = len(str3) - 1
    for i in range(0,length3 + 1):
        print(str3[length3 - i], end = "")

reversestr()

# given a list of names, concatenate them into a single
# string seprated by space

list1 = ["kaushal","aditya","komal","aryan"]
result = " ".join(list1)
print(result)

#python program to check if a given string is a pangram
#contain all letter of the alphabet

import string
s = "The quick brown fox jumps over the lazy dog"
alphabet = set(string.ascii_lowercase)
input_set = set(s.lower())
if alphabet <= input_set:
    print("string is a pangram")
else:
    print("string is not a pangram")

#calculate the area and circumference of a circle given it
#radius area = pi*r*r circum = 2*pi*radius
import numpy as np
radius = float(input("enter a radius of circle:"))
area = np.pi * radius**2
circum = 2*np.pi*radius
print("the circumference is :",round(circum,2))
print("the area is :",round(area,2))

#implement a program that convert a given number of min
#into hours and minutes.
num9 = int(input("enter a minute: "))
hours = num9 // 60
remain = num9 % 60
print(hours,"hours",remain,"minute")

#program to count the number of vowels in string
string3 = "Microsoft Azure"
vowel = "aeiouAEIOU"
num = 0
for i in range(0,10):
    num = string3.count(vowel[i]) + num
print(num)

#program to check if a no is prime.
num = 1
j = 0
for i in range(1,num+1):
    if num % i == 0:
        j = j + 1
    else:
        j = j + 0
if j == 2:
    print("it is a prime no")
elif j < 2 or j > 2:
    print("it is not a prime no")




















