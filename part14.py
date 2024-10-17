# Calculating the Power of a Number
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to calculate the power of a number.
# Example:
# Input: base = 2, exponent = 3
# Output: 8
# Explanation: 2 raised to the power of 3 is 8.

base = int(input("base = "))
exponent = int(input("exponent = "))
power = base ** exponent
print(power)

# Checking for an Anagram
# Difficulty: Easy
# Topics: String Manipulation
# Description: Write a program to check if two strings are anagrams.
# Example:
# Input: string1 = "listen", string2 = "silent"
# Output: True
# Explanation: "listen" and "silent" are anagrams of each other.

str1 = input("string1 = ")
str2 = input("String2 = ")
str1 = list(str1)
str2 = list(str2)
str1.sort
str2.sort
a = 0
for i in range(0,len(str1)):
    for j in range(0,len(str2)):
        if str1[i] == str2[j]:
            a = a + 1
        else:
            a = a + 0
if a == len(str1):
    print(True)
else:
    print(False)

# Finding the Sum of Prime Numbers in a Range
# Difficulty: Medium
# Topics: Number Theory, Mathematical Computations
# Description: Write a program to calculate the sum of all prime numbers within a given range.
# Example:
# Input: range = [1, 10]
# Output: 17
# Explanation: The sum of prime numbers between 1 and 10 is 2 + 3 + 5 + 7 = 17.

num1 = int(input("enter a starting range:"))
num2 = int(input("enter a end range:"))
a = 0
b = 0
for i in range(num1,num2+1):
    for j in range(1,i+1):
        if i % j == 0:
            b = b + 1
        else:
            b = b + 0
    if b == 2:
        a = a + i
    b = 0
print(a)


# Finding the N-th Triangular Number
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to find the N-th triangular number.
# Example:
# Input: N = 4
# Output: 10
# Explanation: The 4th triangular number is 10 (sum of the first 4 natural numbers).

num = int(input("enter a nth number:"))
triangluar = (num)*(num+1) / 2
print(int(triangluar))

# Checking for Perfect Squares
# Difficulty: Easy
# Topics: Mathematical Computations
# Description: Write a program to determine if a number is a perfect square.
# Example:
# Input: number = 16
# Output: True
# Explanation: 16 is a perfect square (4^2 = 16).

num = int(input("enter a number:"))
b = 0
for i in range(0,num+1):
    if i **2 == num:
        b = b + 1
if b == 1:
    print("it is prefect square")
else:
    print("it is not a perfect square")

# Finding the Sum of Squares of Digits
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to find the sum of the squares of the digits of a number.
# Example:
# Input: number = 123
# Output: 14
# Explanation: The sum of the squares of digits is 1^2 + 2^2 + 3^2 = 14.

num = int(input("number:-"))
c =0
while num >0:
    a = num % 10
    c = a**2 + c
    num = num // 10
print(c)

# Generating a Square Matrix of a Given Size
# Difficulty: Medium
# Topics: Arrays, Matrix Operations
# Description: Write a program to generate a square matrix of a given size and fill it with sequential numbers.
# Example:
# Input: size = 3
# Output:
#1 2 3
#4 5 6
#7 8 9
import numpy as np
size = int(input("size:"))
square = (size**2) + 1
array = np.arange(1,square).reshape(size,size)
print(array)


# Calculating the Sum of Digits of a Number Until Single Digit
# Difficulty: Medium
# Topics: Mathematical Computations
# Description: Write a program to keep summing the digits of a number until a single digit is obtained.
# Example:
# Input: number = 9875
# Output: 2
# Explanation: The sum of digits is 9 + 8 + 7 + 5 = 29, and then 2 + 9 = 11, and finally 1 + 1 = 2.

num = int(input('enter a number:'))
b = 0
while num > 10:
    while num > 0:
        a = num % 10
        b = b + a
        num = num // 10
    num = b
    b = 0
print(num)



# Finding the Count of Specific Digits in a Number
# Difficulty: Easy
# Topics: Basic Programming, String Manipulation
# Description: Write a program to count the occurrences of a specific digit in a number.
# Example:
# Input: number = 122333, digit = 3
# Output: 3
# Explanation: The digit 3 occurs 3 times in the number 122333.

def countocc(number,digit):
    a = 0
    count = 0
    while number > 0:
        a = number % 10
        if a == digit:
            count+=1
        number = number // 10
    return count

print(countocc(122333,3))

# Generating a Fibonacci Sequence Using Recursion
# Difficulty: Medium
# Topics: Recursion, Sequences
# Description: Write a recursive program to generate the Fibonacci sequence up to a given number.
# Example:
# Input: number = 5
# Output: 0, 1, 1, 2, 3
# Explanation: The Fibonacci sequence up to 5 is generated.

def fibo(n):
    if n==0 or n ==1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("enter a number:"))
i = 0
while i < n:
    print(fibo(i),end = " ")
    i+=1

# Finding All Divisors of a Number
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to find all divisors of a given number.
# Example:
# Input: number = 12
# Output: 1, 2, 3, 4, 6, 12
# Explanation: The divisors of 12 are 1, 2, 3, 4, 6, and 12.

def alldiv(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=",")

n = int(input("enter a number:"))
alldiv(n)

# Finding the Average of Numbers in an Array
# Difficulty: Easy
# Topics: Arrays, Mathematical Computations
# Description: Write a program to calculate the average of numbers in an array.
# Example:
# Input: array = [1, 2, 3, 4, 5]
# Output: 3
# Explanation: The average of the numbers is (1 + 2 + 3 + 4 + 5) / 5 = 3.

import numpy as np
array = []
number = int(input("enter a number:"))
for i in range(0,number):
    x = int(input(f"enter {i+1} number:-"))
    array.append(x)
array = np.array(array)
print(array)
avg = np.mean(array)
print(int(avg))

# Finding the Mode of Numbers in an Array
# Difficulty: Medium
# Topics: Arrays, Statistical Analysis
# Description: Write a program to find the mode (most frequent number) in an array.
# Example:
# Input: array = [1, 2, 2, 3, 4, 4, 4]
# Output: 4
# Explanation: The most frequent number in the array is 4.

import numpy as np
array = []
num = int(input("enter a number:-"))
for i in range(0,num):
    x = int(input(f"enter {i+1} number:-"))
    array.append(x)
array = np.array(array)
digit = set(array)
a = 0
dict ={}
for i in digit:
    for j in array:
        if i == j:
            a +=1
    dict.update({i:a})
    a = 0


Key_max = max(dict, key = dict.get)
print(Key_max)









