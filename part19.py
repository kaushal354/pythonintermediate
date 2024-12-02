# Generating a Pattern of Increasing Numbers
# Difficulty: Easy
# Topics: Patterns
# Description: Write a program to create a pattern where numbers increase with each row.
# Example:
# Input: rows = 3
# Output:
# 1
# 12
# 123
rows = int(input("enter a number:"))
for i in range(rows):
    for j in range(0,i+1):
        print(j+1,end = " ")
    print()

# Finding the Largest Element in Each Row of a Matrix
# Difficulty: Easy
# Topics: Matrix Operations
# Description: Write a program to find the largest element in each row of a matrix.
# Example:
# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [3, 6, 9]
# Explanation: The largest elements in each row are 3, 6, and 9.
matrix = [[1,2,3],[4,5,6],[7,8,9]]
maxel = []
for i in range(0,len(matrix)):
    maxel.append(max(matrix[i]))
print(maxel)



# Checking for Anagram Pairs in a List of Strings
# Difficulty: Medium
# Topics: String Manipulation
# Description: Write a program to find pairs of strings in a list that are anagrams of each other.
# Example:
# Input: strings = ["listen", "silent", "hello", "world"]
# Output: [("listen", "silent")]
# Explanation: "listen" and "silent" are anagrams.
string = ["listen","silent","hello","world"]
anagram = []
count = 0
for i in range(0,len(string)):
    a = string[i]
    for j in range(0,len(string)):
        if j != i:
            b = string[j]
            if len(b) == len(a):
                for k in range(0,len(b)):
                    for l in range(0,len(b)):
                        if a[k] == b[l]:
                            count +=1
                    if count == len(a):
                        anagram.append(a)
                count = 0
print(anagram)



# Finding the Frequency of Each Character in a String
# Difficulty: Easy
# Topics: String Manipulation
# Description: Write a program to count the frequency of each character in a given string.
# Example:
# Input: string = "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# Explanation: The frequency of each character in the string "hello" is shown.
string = "hello"
string1 = list(set(string))
count = {}
k = 0
for i in range(0,len(string1)):
    for j in range(0,len(string)):
        if string1[i]==string[j]:
            k+=1
            count.update({string1[i]:k})
    k = 0

print(count)


# Generating a Matrix with Random Numbers
# Difficulty: Easy
# Topics: Random Number Generation, Matrix Operations
# Description: Write a program to generate a matrix filled with random numbers.
# Example:
# Input: rows = 2, columns = 3
# Output:
# 3 8 1
# 7 4 6
import random
import numpy as np
rows = int(input("enter a rows:"))
column = int(input("enter a column"))
matrix = np.zeros((2,3),dtype=int)
for i in range(0,rows):
    j = i+1
    for k in range(0,column):
        matrix[i:j,k] = random.randint(0,9)
print(matrix)

# Finding the Length of the Longest Word in a String
# Difficulty: Easy
# Topics: String Manipulation
# Description: Write a program to find the length of the longest word in a given string.
# Example:
# Input: string = "Find the longest word"
# Output: 7
# Explanation: The longest word is "longest" with length 7.
string = "Find the longest word"
b = string.split(" ")
a = 0
for i in range(0,len(b)):
    if len(b[i])>a:
        word = b[i]
        a = len(b[i])
print(a,word)




# Finding All Triplets in an Array That Sum to Zero
# Difficulty: Medium
# Topics: Arrays, Sorting
# Description: Write a program to find all unique triplets in an array that sum to zero.
# Example:
# Input: array = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1],]
# Explanation: The unique triplets that sum to zero are listed.
from itertools import combinations
array = [-1,0,1,2,-1,-4]
a = 0
uni = []
all_triplet = list(combinations(array,3))
for triplet in all_triplet:
    if sum(triplet) == 0:
        uni.append(triplet)
print(uni)



# Generating a Square Matrix with Random Values
# Difficulty: Easy
# Topics: Random Number Generation, Matrix Operations
# Description: Write a program to generate a square matrix where each element is a random value.
# Example:
# Input: size = 3
# Output:
# 7 3 5
# 2 6 9
# 1 8 4
import numpy as np
import random
size = int(input("enter a size:-"))
matrix = np.zeros((size,size),dtype=int)
for i in range(0,size):
    j = i+1
    for k in range(0,size):
        matrix[i:j,k] = random.randint(0,9)

print(matrix)



# Finding the Difference Between the Sum of Even and Odd Numbers in an Array
# Difficulty: Easy
# Topics: Arrays, Mathematical Computations
# Description: Write a program to calculate the difference between the sum of even and odd numbers in an array.
# Example:
# Input: array = [1, 2, 3, 4, 5, 6]
# Output: 3
# Explanation: The sum of even numbers is 12, and the sum of odd numbers is 9. The difference is 3.
array = [1,2,3,4,5,6]
even = 0
odd = 0
for i in array:
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
diff = even - odd
print(diff)


# Generating a Triangle Pattern of Stars with a Given Height
# Difficulty: Easy
# Topics: Patterns
# Description: Write a program to create a triangle pattern of stars with a specified height.
# Example:
# Input: height = 4
# Output:
# *
# **
# ***
# ****

height = int(input("enter a height:"))
for i in range(height):
    for j in range(0,i+1):
        print("*",end = " ")
    print()
