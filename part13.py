# #Finding the Fibonacci Number at a Specific Position
# # Difficulty: Easy
# # Topics: Basic Programming, Sequences
# # Description: Write a program to find the Fibonacci number at a specific position.
# # Example:
# # Input: position = 5
# # Output: 5
# # Explanation: The Fibonacci number at position 5 is 5 (sequence: 0, 1, 1, 2, 3, 5).

# num = int(input("position = "))
# a = 0
# b = 1
# for i in range(0,num-1):
#     if a < b:
#         a = a + b
#     else:
#         b = a + b

# if a < b:
#     print(b)
# else:
#     print(a)

# # Printing Prime Numbers Less Than a Given Number
# # Difficulty: Easy
# # Topics: Basic Programming, Number Theory
# # Description: Write a program to print all prime numbers less than a given number.
# # Example:
# # Input: number = 20
# # Output: 2, 3, 5, 7, 11, 13, 17, 19
# # Explanation: The prime numbers less than 20 are 2, 3, 5, 7, 11, 13, 17, and 19.

# num = int(input("number:"))
# b = 0
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         if i % j == 0:
#             b = b + 1
#         else:
#             b = b + 0
#     if b == 2:
#         print(i,end=" ")
#     b = 0

# # Finding the Number of Digits in a Number
# # Difficulty: Easy
# # Topics: Basic Programming, Mathematical Computations
# # Description: Write a program to count the number of digits in a given number.
# # Example:
# # Input: number = 12345
# # Output: 5
# # Explanation: The number 12345 has 5 digits.

# num = int(input("number = "))
# b = 0
# while num > 0:
#     num = num // 10
#     b = b + 1
# print(b)

# # Checking if a Number is a Narcissistic Number
# # Difficulty: Easy
# # Topics: Basic Programming, Number Theory
# # Description: Write a program to check if a number is a narcissistic number (where the sum of its digits raised to the power of the number of digits equals the number itself).
# # Example:
# # Input: number = 153
# # Output: Narcissistic Number
# # Explanation: 153 is a narcissistic number because 1^3 + 5^3 + 3^3 = 153.

# num = int(input("number = "))
# num1 = num
# num2 = num
# b = 0
# while num1 > 0:
#     num1 = num1 // 10
#     b = b + 1

# a = 0
# while num > 0:
#     a = (num % 10)**b + a
#     num = num // 10

# if a == num2:
#     print("Narcissistic number")
# else:
#     print("not Narcissistic number")

# # Generating a Pattern of Numbers
# # Difficulty: Easy
# # Topics: Basic Programming, Patterns
# # Description: Write a program to generate number patterns (e.g., sequential numbers in a matrix).
# # Example:
# # Input: rows = 3
# # Output:
# #1
# #23
# #456

# num = int(input("rows = "))
# a = 0
# for i in range(num):
#     for j in range(0,i+1):
#         a = a+1
#         print(a,end= " ")
#     print()


# # Finding the Sum of the Digits of the Factorial of a Number
# # Difficulty: Easy
# # Topics: Basic Programming, Mathematical Computations
# # Description: Write a program to find the sum of the digits of the factorial of a given number.
# # Example:
# # Input: number = 4
# # Output: 6
# # Explanation: The factorial of 4 is 24, and the sum of the digits (2 + 4) is 6.

# num = int(input("number = "))
# a = 1
# for i in range(num,0,-1):
#     a = i * a
# b=0
# while a > 0:
#     c = a % 10
#     b = b + c
#     a = a // 10

# print(b)

# Finding the Largest Palindrome in a String
# Difficulty: Easy
# Topics: Basic Programming, String Manipulation
# Description: Write a program to find the largest palindrome in a given string.
# Example:
# Input: string = "babad"
# Output: "bab" or "aba"
# Explanation: Both "bab" and "aba" are valid palindromes in the string.

str1 = input("string = ")
x = []
k = 0
l = 0
while l < len(str1)-1:
    l +=1
    if str1[k] == str1[l]:
        substr = str1[k : l+1]
        substr2 = substr
        b = len(substr) // 2
        a = 0
        c = len(substr)-1
        for j in range(0,b):
            if substr[j] == substr2[c]:
                a = a + 1
                c -= 1
        if a == b:
            x.append(substr)
        else:
            l = 0
            l = k+1
        a = 0
        k +=1
    if l >=len(str1)-1:
        l = 0
        l = k + 1
        k+=1

print(x)

# # Finding Missing Numbers in a Sequence
# # Difficulty: Easy
# # Topics: Basic Programming, Arrays
# # Description: Write a program to find missing numbers in a sequence from 1 to n.
# # Example:
# # Input: sequence = [1, 2, 4, 5]
# # Output: [3]
# # Explanation: The missing number in the sequence from 1 to 5 is 3.
# sequence = [1,2,4,5]
# missing = []
# lastnum = sequence[len(sequence)-1]
# a =0
# for i in range(1, lastnum):
#     for j in range(0,len(sequence)):
#         if sequence[j] == i:
#             a+= 1
#         else:
#             a+= 0
#     if a == 0:
#         missing.append(i)
#     a = 0

# print(missing)

# #Generating a Pascal’s Triangle
# # Difficulty: Medium
# # Topics: Arrays, Mathematical Computations
# # Description: Write a program to generate Pascal's Triangle up to a given number of rows.
# # Example:
# # Input: rows = 4
# # Output:
# #1
# #11
# #121
# #1331
# num = int(input("rows = "))
# a = 11
# num1 = []
# for i in range(num):
#     a = a**i
#     while a >0:
#         num1.append(a%10)
#         a = a // 10
#     for j in range(0,i+1):
#         print(num1[j],end=" ")
#     print()
#     a = 11
#     num1 = []

# # Finding the Median of an Array
# # Difficulty: Medium
# # Topics: Arrays, Sorting
# # Description: Write a program to find the median of an array of numbers.
# # Example:
# # Input: array = [3, 1, 2, 4, 5]
# # Output: 3
# # Explanation: The median of the sorted array [1, 2, 3, 4, 5] is 3.
# import numpy as np
# array = np.array([3,1,2,4,5])
# array.sort()
# n = len(array) // 2
# if len(array) % 2 == 0:
#     print(array[n-1],array[n])
# else:
#     print(array[n])








