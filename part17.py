# Finding the Longest Consecutive Sequence in an Array
# Difficulty: Medium
# Topics: Arrays, Hashing
# Description: Write a program to find the longest sequence of consecutive numbers in an array.
# Example:
# Input: array = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive sequence is [1, 2, 3, 4].

array = [2,6,1,9,4,5,3]
array.sort()
num1 = 0
j = 0
count = 0
for i in range(array[0],array[len(array)-1]):
    if array[j] == i:
        count+=1
        j+=1
    else:
        if count>num1:
            num1 = count+num1
            count = 0
print(num1)


# Generating a Matrix with a Spiral Pattern
# Difficulty: Medium
# Topics: Arrays, Matrix Operations
# Description: Write a program to generate a matrix filled with numbers in a spiral pattern.
# Example:
# Input: size = 3
# Output:
# 123
# 894
# 765

import numpy as np

# Input size of the array
size = int(input("Enter the size of the array: "))

# Initialize an empty 2D array
array = np.zeros((size, size), dtype=int)

# Initialize variables
top, left = 0, 0
bottom, right = size - 1, size - 1
num = 1

# Fill the array in spiral order
while top <= bottom and left <= right:
    # Fill the top row
    for i in range(left, right + 1):
        array[top][i] = num
        num += 1
    top += 1

    # Fill the right column
    for i in range(top, bottom + 1):
        array[i][right] = num
        num += 1
    right -= 1

    # Fill the bottom row
    if top <= bottom:
        for i in range(right, left - 1, -1):
            array[bottom][i] = num
            num += 1
        bottom -= 1

    # Fill the left column
    if left <= right:
        for i in range(bottom, top - 1, -1):
            array[i][left] = num
            num += 1
        left += 1

# Print the spiral pattern
print("Spiral pattern:")
print(array)




# Finding All Subsets of a Set
# Difficulty: Medium
# Topics: Combinatorics
# Description: Write a program to generate all possible subsets of a given set of numbers.
# Example:
# Input: set = [1, 2]
# Output: [[], [1], [2], [1, 2]]
# Explanation: The subsets of [1, 2] are the empty set, [1], [2], and [1, 2].

set1 = [1, 2, 3,4]
subset = []

# Total number of subsets is 2^len(set1)
len1 = 2 ** len(set1)

# Generate subsets using binary representation
for i in range(len1):
    temp_subset = []
    for j in range(len(set1)):
        # Check if jth element is included in the ith subset
        if i & (1 << j):
            temp_subset.append(set1[j])
    subset.append(temp_subset)

# Print all subsets
print("Subsets:", subset)









# Checking for Perfect Squares in a Range
# Difficulty: Easy
# Topics: Mathematical Computations
# Description: Write a program to check which numbers in a given range are perfect squares.
# Example:
# Input: start = 1, end = 10
# Output: [1, 4, 9]
# Explanation: Perfect squares between 1 and 10 are 1, 4, and 9.
start = int(input("enter a starting range:"))
end = int(input("enter a ending range:"))
perfectsq = []
for i in range(start,end+1):
    if i**2 < end:
        perfectsq.append(i**2)
print(perfectsq)

# Finding the Sum of Diagonal Elements in a Matrix
# Difficulty: Easy
# Topics: Matrix Operations
# Description: Write a program to calculate the sum of the diagonal elements in a square matrix.
# Example:
# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: 15
# Explanation: The sum of the diagonal elements (1 + 5 + 9) is 15

import numpy as np
matrix = np.arange(1,10).reshape(3,3)
a = np.diagonal(matrix)
print(sum(a))

# Finding the Second Smallest Number in an Array
# Difficulty: Easy
# Topics: Arrays
# Description: Write a program to find the second smallest number in an array.
# Example:
# Input: array = [12, 13, 1, 10, 34, 1]
# Output: 10
# Explanation: The second smallest number in the array is 10.

array = [12,13,1,10,34,1]
array.sort()
i = 0
count = 0
for i in range(0,len(array)+1):
    if array[0]==array[i]:
        i=i+1
    else:
        print(array[i])
        break


# Generating Pascal’s Triangle Up to N Rows
# Difficulty: Medium
# Topics: Combinatorics
# Description: Write a program to generate Pascal’s Triangle up to N rows.
# Example:
# Input: N = 3
# Output:
# 1
# 1 1
# 1 2 1
num = int(input("rows = "))
a = 11
num1 = []
for i in range(num):
    a = a**i
    while a >0:
        num1.append(a%10)
        a = a // 10
    for j in range(0,i+1):
        print(num1[j],end=" ")
    print()
    a = 11
    num1 = []


# Finding the Sum of Digits of the Product of Two Numbers
# Difficulty: Easy
# Topics: Mathematical Computations
# Description: Write a program to find the sum of the digits of the product of two given numbers.
# Example:
# Input: number1 = 12, number2 = 34
# Output: 9
# Explanation: The product of 12 and 34 is 408, and the sum of its digits is 4 + 0 + 8 = 12.
num1 = int(input("enter a first number:"))
num2 = int(input("enter a second number:"))
product = num1 * num2
b = 0
while product>0:
    a = product % 10
    product = product // 10
    b = b + a

print("sum of its digit is:",b)


# Checking for Palindromic Numbers in a Range
# Difficulty: Medium
# Topics: Mathematical Computations
# Description: Write a program to check for palindromic numbers within a given range.
# Example:
# Input: start = 1, end = 100
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
# Explanation: Palindromic numbers between 1 and 100 are the numbers listed.
start = int(input("enter a starting range:"))
end = int(input("enter a ending range:"))
num = []
count = 0
palindromicnum = []
for i in range(start,end+1):
    if i >=10:
        tempi = i
        while tempi >0:
            a = tempi % 10
            tempi = tempi // 10
            num.append(a)
        loop = len(num) //2
        for j in range(0,loop):
            if num[j] == num[(len(num)-1)-j]:
                count+=1
        if count == loop:
            palindromicnum.append(i)
    if i<10:
        palindromicnum.append(i)
    count = 0
    num = []

print(palindromicnum)



# Generating a Matrix with Alternating 0s and 1s
# Difficulty: Easy
# Topics: Arrays, Matrix Operations
# Description: Write a program to generate a matrix where the elements alternate between 0 and 1.
# Example:
# Input: size = 3
# Output:
# 0 1 0
# 1 0 1
# 0 1 0
import numpy as np
a = np.zeros((3,3),dtype=int)
num = [0,1]
l = 0
for i in range(0,3):
    for j in range(1,4):
        for k in range(0,3):
            a[i:j,k] = l
            if l == 0:
                l = 1
            else:
                l = 0

print(a)



# Finding the Count of a Specific Word in a String
# Difficulty: Easy
# Topics: String Manipulation
# Description: Write a program to count how many times a specific word appears in a given string.
# Example:
# Input: string = "hello world hello"
# Output: 2
# Explanation: The word "hello" appears 2 times in the string.
str1 = "hello world hello"
a = str1.split()
b = set(a)
count = 0
for i in b:
    for j in a:
        if i== j:
            count+=1
    if count > 1:
        print(i,"=",count)
    count = 0

# Finding the Largest Sum of a Subarray
# Difficulty: Medium
# Topics: Arrays, Dynamic Programming
# Description: Write a program to find the largest sum of any contiguous subarray.
# Example:
# Input: array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The largest sum is 6, from the subarray [4, -1, 2, 1].

array = [-2,1,-3,4,-1,2,1,-5,4]
num = []
j = 0
for k in range(1,len(array)):
    for i in range(0,len(array)-k):
        a = array[i:i+k]
        print(a)
        b = sum(a)
        if b > j:
            j = b

print(j)

