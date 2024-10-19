# Determining the Length of a String Without Using Built-In Functions
# Difficulty: Medium
# Topics: String Manipulation
# Description: Write a program to determine the length of a string without using built-in functions.
# Example:
# Input: string = "hello"
# Output: 5
# Explanation: The length of the string "hello" is determined without using built-in functions.

str1 = input("enter a str:")
count = 0
for i in str1:
    count+=1

print(count)

#Generating a Number Pyramid
# Difficulty: Medium
# Topics: Patterns, Basic Programming
# Description: Write a program to generate a pyramid of numbers (e.g., 1, 12, 123, etc.).
# Example:
# Input: rows = 4
# Output:
# 1
# 12
# 123
# 1234

Explanation: A number pyramid with 4 rows is generated.



rows = int(input("rows:"))
for i in range(rows):
    for j in range(1,i+2):
        print(j,end = " ")
    print()

# Finding the Sum of Prime Factors of a Number
# Difficulty: Medium
# Topics: Number Theory, Mathematical Computations
# Description: Write a program to find the sum of the prime factors of a given number.
# Example:
# Input: number = 12
# Output: 5
# Explanation: The prime factors of 12 are 2 and 3, and their sum is 2 + 3 = 5


num = int(input("number:"))
b = 0
x = []
for i in range(num):
    for j in range(1,i+1):
        if i % j ==0:
            b = b + 1
        else:
            b = b + 0
    if b == 2:
        x.append(i)
    b = 0

primenum = []
for i in x:
    if num % i == 0:
        primenum.append(i)

sum  = sum(primenum)
print(sum)

# Finding the Second Largest Number in an Array
# Difficulty: Medium
# Topics: Arrays, Sorting
# Description: Write a program to find the second largest number in an array.
# Example:
# Input: array = [10, 20, 4, 45, 99]
# Output: 45
# Explanation: The second largest number in the array is 45.

import numpy as np
num = int(input("how much element you want to insert in array:"))
array = []
for i in range(num):
    x = int(input(f"enter a {i+1} element for array"))
    array.append(x)

array = np.array(array)
array.sort()
print(array[len(array) - 2])

# Finding the Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topics: String Manipulation, Sliding Window
# Description: Write a program to find the longest substring without repeating characters in a given string.
# Example:
# Input: string = "abcabcbb"
# Output: "abc"
# Explanation: The longest substring without repeating characters is "abc".

str = input("enter a string:")
sub = ""
count = 0
for i in range(0,len(str)+1):
    for j in range(i,len(str)+1):
            substr = str[i:j]
            sub1 = list(set(substr))
            for k in range(0,len(sub1)):
                for l in range(0,len(substr)):
                    if sub1[k] == substr[l]:
                        count += 1
            if count == len(sub1):
                if len(sub) <len(substr):
                    sub = substr
            count = 0


print(sub)

# Finding the Sum of Digits of a Number Until Zero
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to repeatedly sum the digits of a number until the result is zero.
# Example:
# Input: number = 123
# Output: 6
# Explanation: Sum of digits is 1 + 2 + 3 = 6; sum of digits of 6 is 6 (which is a single digit).


num = int(input("enter:"))
b = 0
while num > 0:
    a = num% 10
    b = b + a
    num = num // 10

print(b)

# Generating a Multiplication Table for a Range
# Difficulty: Easy
# Topics: Arrays, Basic Programming
# Description: Write a program to generate multiplication tables for numbers within a specified range.
# Example:
# Input: start = 2, end = 4
# Output:
# 2 x 1 = 2   3 x 1 = 3   4 x 1 = 4
# 2 x 2 = 4   3 x 2 = 6   4 x 2 = 8
# 2 x 3 = 6   3 x 3 = 9   4 x 3 = 12
# 2 x 4 = 8   3 x 4 = 12  4 x 4 = 16

start = int(input("enter starting range:"))
end = int(input("enter a ending range:"))
for i in range(start,end+1):
    print("\n")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")



# Calculating the Sum of a Series (1 + 1/2 + 1/3 + ... + 1/n)
# Difficulty: Medium
# Topics: Mathematical Computations
# Description: Write a program to calculate the sum of the series 1 + 1/2 + 1/3 + ... + 1/n up to the nth term.
# Example:
# Input: n = 4
# Output: 2.083333
# Explanation: Sum of the series is 1 + 1/2 + 1/3 + 1/4 ≈ 2.083333.

num = int(input("enter a number:"))
a =0
for i in range(1,num+1):
    a = a + (1/i)
print(a)

# Finding All Pairs of Elements in an Array that Add Up to a Given Sum
# Difficulty: Medium
# Topics: Arrays, Hashing
# Description: Write a program to find all pairs of elements in an array whose sum equals a specified target.
# Example:
# Input: array = [1, 2, 3, 4, 5], target = 5
# Output: [(1, 4), (2, 3)]
# Explanation: Pairs that sum up to 5 are (1, 4) and (2, 3).

array = [1,2,3,4,5]
num1 = []
num = []
target = int(input("enter a target:"))
for i in range(0,len(array)):
    for j in range(0,len(array)):
        if array[i] + array[j] == target:
            num1.append(array[i])
            num1.append(array[j])
            num1.sort()
            num.append(tuple(num1))
            num1.clear()

print(set(num))


# Generating a Diamond Pattern of Stars
# Difficulty: Medium
# Topics: Patterns, Basic Programming
# Description: Write a program to create a diamond pattern with stars of a given size.
# Example:
# Input: size = 5
# Output:
#   *
#  ***
# *****
#  ***
#   *

n = 3
for i in range(n-1):
    for j in range(i,n):
        print(" ",end = " ")
    for j in range(i):
        print("*",end = " ")
    for j in range(i+1):
        print("*",end = " ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end = " ")
    for j in range(i,n-1):
        print("*",end = " ")
    for j in range(i,n):
        print("*",end = " ")
    print()




















