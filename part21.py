# Problem 11: Print a Pattern of Alternating 0s and 1s
# Difficulty: Medium
# Topics: Matrix Pattern
# Hint: Print a matrix where elements alternate between 0 and 1.
# The pattern should alternate both row-wise and column-wise.
# Example 1: Input: n = 4
# Output:
# 0101
# 1010
# 0101
# 1010
import numpy as np
num = int(input("enter a number n:"))
matrix = np.zeros((num,num),dtype=int)
l = 0
for i in range(0,num):
    j=i+1
    for k in range(0,num):
        matrix[i:j,k] = l
        if l==0:
            l=1
        else:
            l=0
    if l==0:
        l=1
    else:
        l=0
print(matrix)



# Problem 12: Print a Pascal’s Triangle
# Difficulty: Medium
# Topics: Matrix Pattern
# Hint: Print Pascal’s Triangle up to N rows.
# Each row should be constructed based on the sum of the elements directly above it in the previous row.
# Example 1: Input: n = 4
# Output:
#    1
#   1 1
#  1 2 1
# 1 3 3 1

num = int(input("enter a number:"))
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

num = int(input("Enter the number of rows: "))  # Input for number of rows
triangle = []  # List to store each row of the triangle

for i in range(num):
    row = [1]  # Start each row with 1
    if i > 0:
        # Generate the inner values of the row based on the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with 1
    triangle.append(row)  # Add the row to the triangle

    # Print the row with proper spacing
    print(' '.join(map(str, row)).center(2 * num))




# Problem 13: Print a Pattern of Consecutive Numbers
# Difficulty: Medium
# Topics: Matrix Pattern
# Hint: Print a matrix of consecutive numbers starting from 1, filling rows sequentially.
# Example 1: Input: n = 3
# Output:
# 1 2 3
# 4 5 6
# 7 8 9
import numpy as np
num = 3
l = 1
matrix = np.zeros((num,num),dtype=int)
for i in range(num):
    j=i+1
    for k in range(num):
        matrix[i:j,k] = l
        l+=1
print(matrix)


# Problem 14: Print a Star Pattern with Increasing Width
# Difficulty: Medium
# Topics: Pattern Printing
# Hint: Print a pattern where each row has an increasing width of stars.
# Example 1: Input: n = 3
# Output:
# *
# ***
# *****
num = 3
l =0
for i in range(num):
    if i==0:
        a = 1
    else:
        a = l
    for j in range(a):
        print("*",end=" ")
    print()
    l+=3


# Problem 15: Print a Right-Angle Triangle Pattern with Characters
# Difficulty: Medium
# Topics: Pattern Printing
# Hint: Print a right-angle triangle pattern using characters.
# Each row should contain the same character repeated according to the row number.
# Example 1: Input: n = 3
# Output:
# A
# BB
# CCC
import string
alpha = string.ascii_uppercase
num = 3
for i in range(num):
    for k in range(i+1):
        print(alpha[i],end=" ")
    print()


# Problem 16: Print a Checkerboard Pattern
# Difficulty: Medium
# Topics: Matrix Pattern
# Hint: Print a checkerboard pattern with two different characters alternating.
# Example 1: Input: n = 4
# Output:
# XOXOXO
# OXOXOX
# XOXOXO
# OXOXOX
num = int(input("enter a number:"))
l = "XO"
for i in range(num):
    for j in range(num-1):
        print(l,end=" ")
    if l=="XO":
        l="OX"
    else:
        l="XO"
    print()


# Problem 17: Print a Pyramid Pattern of Increasing Stars
# Difficulty: Medium
# Topics: Pattern Printing
# Hint: Print a pyramid pattern where each row increases in the number of stars.
# Example 1: Input: n = 3
# Output:
#   *
#  ***
# *****
num = int(input("enter a number:"))
for i in range(0,num):
    for j in range(i,num):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()


# Problem 18: Print a Border Pattern with Numbers
# Difficulty: Medium
# Topics: Matrix Pattern
# Hint: Print a border pattern using numbers.
# The border should be filled with numbers, and the inner part should be empty.
# Example 1: Input: n = 4
# Output:
# 1234
# 1  1
# 1  1
# 1234
num = int(input("enter a number:"))
k = 1
for i in range(num):
    for j in range(num):
        if i ==0 or i == num-1:
            print(k,end=" ")
            k+=1
        else:
            if j ==0 or j == num-1:
                print(k,end=" ")
            else:
                print(" ",end=" ")
    k=1
    print()


# Problem 19: Print an Inverted Pyramid Pattern with Characters
# Difficulty: Medium
# Topics: Pattern Printing
# Hint: Print an inverted pyramid pattern using characters.
# Each row should have decreasing characters from the top row.
# Example 1: Input: n = 3
# Output:
# CCC
#  BB
#   A
import string
alpha = string.ascii_uppercase
print(alpha)
num = int(input("enter a number:"))
l = num-1
for i in range(num):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,num):
        print(alpha[l],end=" ")
    l-=1
    print()

# Problem 20: Print a Cross Pattern with Stars
# Difficulty: Medium
# Topics: Pattern Printing
# Hint: Print a cross pattern using stars.
# The cross should be centered within a matrix.
# Example 1: Input: n = 5
# Output:
# *   *
#  * *
#   *
#  * *
# *   *

num = int(input("enter a number:"))
l=0
k = num-1
for i in range(num):
    for j in range(num):
        if i==l and j == l:
            print("*",end=" ")
        elif i ==l and j==k:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    l+=1
    k-=1
    print()

