# Reversing a String
# Difficulty: Easy
# Topics: Basic Programming, String Manipulation
# Description: Write a program to reverse a given string.
# Example:
# Input: string = "programming"
# Output: "gnimmargorp"
# Explanation: The reversed string of "programming" is "gnimmargorp".

str1 = "programming"
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end="")

# Finding the Largest and Smallest Numbers in an Array
# Difficulty: Easy
# Topics: Basic Programming, Arrays
# Description: Write a program to find the largest and smallest numbers in an array.
# Example:
# Input: array = [4, 7, 1, 8, 5]
# Output: Largest: 8, Smallest: 1
# Explanation: The largest number in the array is 8 and the smallest is 1.

list1 = [4,7,1,8,5]
list1.sort()
print(f"Largest: {list1[len(list1)-1]}, Smallest: {list1[0]}")

# Sorting an Array
# Difficulty: Easy
# Topics: Basic Programming, Sorting Algorithms
# Description: Write a program to sort an array of numbers in ascending order.
# Example:
# Input: array = [3, 1, 4, 1, 5, 9]
# Output: [1, 1, 3, 4, 5, 9]
# Explanation: The array sorted in ascending order is [1, 1, 3, 4, 5, 9].

list1 = []
a = int(input("how much element you want to add in array:"))
for i in range(0,a):
    b = int(input(f"{i+1} elements"))
    list1.append(b)
print(f"array = {list1}")
list1.sort()
print(list1)

# Finding the Sum of Elements in an Array
# Difficulty: Easy
# Topics: Basic Programming, Arrays
# Description: Write a program to find the sum of elements in an array.
# Example:
# Input: array = [1, 2, 3, 4, 5]
# Output: 15
# Explanation: The sum of the elements in the array is 15.
list2 = []
a = int(input("how much element you want to add in array:"))
for i in range(0,a):
    b = int(input(f"{i+1} elemets"))
    list2.append(b)
print(f"array = {list2}")
print(sum(list2))

# Checking for Armstrong Numbers in a Range
# Difficulty: Easy
# Topics: Basic Programming, Number Theory
# Description: Write a program to find all Armstrong numbers within a given range.
# Example:
# Input: range = [1, 500]
# Output: [1, 153, 370, 371, 407]
# Explanation: Armstrong numbers between 1 and 500 are 1, 153, 370, 371, and 407.
start = int(input("starting range:"))
end = int(input("enter a ending range:"))
b = 0
count = 0
for i in range(start,end+1):
    d = str(i)
    e = len(d)
    c = i
    while c != 0:
        a = c % 10
        b = a**e + b
        c = c // 10
    if b == i:
        print(i,end=" ")
    else:
        pass
    b = 0
    count = 0

# Generating Multiplication Tables
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to generate multiplication tables for a given number.
# Example:
# Input: number = 4
# Output:
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# Explanation: The multiplication table for 4 up to 5 is generated.
num = int(input("enter a number which table you want to print:"))
for i in range(1,6):
    print(f"{num} x {i} = {num*i}")

# Finding Prime Numbers in a Range
# Difficulty: Easy
# Topics: Basic Programming, Number Theory
# Description: Write a program to find all prime numbers within a given range.
# Example:
# Input: range = [10, 30]
# Output: [11, 13, 17, 19, 23, 29]
# Explanation: Prime numbers between 10 and 30 are 11, 13, 17, 19, 23, and 29.
start = int(input("enter a starting range:"))
end = int(input("enter a ending range:"))
b = 0
for i in range(start,end+1):
    for j in range(1,i+1):
        if i % j == 0:
            b = b + 1
        else:
            b = b + 0
    if b == 2:
        print(i,end=" ")
    b = 0

# Checking for Perfect Numbers
# Difficulty: Easy
# Topics: Basic Programming, Number Theory
# Description: Write a program to determine if a number is a perfect number.
# Example:
# Input: number = 28
# Output: Perfect Number
# Explanation: 28 is a perfect number because its divisors (1, 2, 4, 7, 14) sum up to 28.
num = int(input("enter a number:"))
a = 0
for i in range(1,num+1):
    if num % i == 0:
        if num != i:
            a = a + i
if a == num:
    print("perfect")
else:
    print("it is not a perfect")

# Calculating the Sum of Even Numbers in a Range
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to find the sum of all even numbers within a given range.
# Example:
# Input: range = [1, 10]
# Output: 30
# Explanation: The sum of even numbers between 1 and 10 is 2 + 4 + 6 + 8 + 10 = 30
start = int(input("enter a starting range:"))
end = int(input("enter a end range:"))
a = 0
for i in range(start,end+1):
    if i % 2 == 0:
        if i != 1:
            a = a + i
print(a)

# Calculating the Sum of Odd Numbers in a Range
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to find the sum of all odd numbers within a given range.
# Example:
# Input: range = [1, 10]
# Output: 25
# Explanation: The sum of odd numbers between 1 and 10 is 1 + 3 + 5 + 7 + 9 = 25.
start = int(input("enter a starting range:"))
end = int(input("enter a end range:"))
a = 0
for i in range(start,end+1):
    if i & 1 == 1:
        a = a + i


print(a)



