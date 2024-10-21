# # Counting the Number of Palindromic Substrings in a String
# # Difficulty: Medium
# # Topics: String Manipulation
# # Description: Write a program to count how many palindromic substrings exist in a given string.
# # Example:
# # Input: string = "aaa"
# # Output: 6
# # Explanation: Palindromic substrings are "a", "a", "a", "aa", "aa", "aaa".

# str = "abbaeae"
# count1 = 0
# count = 0
# for i in range(0,len(str)):
#     for j in range(i,len(str)):
#         if str[i] == str[j]:
#             substring = str[i:j+1]
#             substring2 = substring
#             len1 = len(substring) // 2
#             len2 = len(substring)
#             if len2 <= 3:
#                 print(substring)
#                 count1 += 1
#             else:
#                 for i in range(0,len1):
#                     if substring[i] == substring2[(len2-1)-i]:
#                         count+=1
#                 if count == len1:
#                     print(substring)
#                     count1 += 1
#                 count = 0


# print(count1)


# # Generating a Matrix with Multiplication Table
# # Difficulty: Easy
# # Topics: Arrays, Matrix Operations
# # Description: Write a program to generate a matrix where each element at position (i, j) is the product of i and j.
# # Example:
# # Input: size = 3
# # Output:
# # 123
# # 246
# # 369

# import numpy as np
# size = int(input("enter a size:"))
# array = np.arange(1,(size**2)+1).reshape(size,size)
# count = 1
# for i in range(0,size):
#     j = i+1
#     for k in range(0,size):
#         array[i:j,k] =  (i+1) * count
#         count += 1
#     j = 0
#     i=0
#     count = 1

# print(array)

# # Finding the GCD of Multiple Numbers
# # Difficulty: Medium
# # Topics: Mathematical Computations
# # Description: Write a program to find the GCD (Greatest Common Divisor) of an array of numbers.
# # Example:
# # Input: array = [12, 24, 36]
# # Output: 12
# # Explanation: The GCD of 12, 24, and 36 is 12.

# num = int(input("enter a size of array"))
# array = []
# for i in range(1,num+1):
#     x = int(input(f"enter a {i} element"))
#     array.append(x)
# cd = []
# gcd = []
# count = 0
# for num in array:
#     for i in range(1,num+1):
#         if num % i == 0:
#             cd.append(i)
# cd = list(set(cd))
# cd.sort()
# for i in range(0,len(cd)):
#     count = 0
#     for num in array:
#         if num % cd[i] == 0 :
#             count += 1
#         if count == len(array):
#             gcd.append(cd[i])

# print(max(gcd))

# # Finding the Sum of the First N Odd Numbers
# # Difficulty: Easy
# # Topics: Mathematical Computations
# # Description: Write a program to calculate the sum of the first N odd numbers.
# # Example:
# # Input: N = 5
# # Output: 25
# # Explanation: Sum of the first 5 odd numbers (1 + 3 + 5 + 7 + 9) is 25.

# num = int(input("enter a number:"))
# list = []
# num = num * 2
# for i in range(1,num+1):
#     if i % 2 == 0:
#         pass
#     else:
#         list.append(i)
# print(sum(list))

# # Finding the Number of Perfect Numbers Up to a Given Limit
# # Difficulty: Medium
# # Topics: Number Theory
# # Description: Write a program to find how many perfect numbers exist up to a given limit.
# # Example:
# # Input: limit = 30
# # Output: 1
# # Explanation: There is only one perfect number (6) up to 30.

# limit = int(input("limit:-"))
# list1 = []
# perfect = []
# count = 0
# for i in range(1,limit+1):
#     for j in range(1,i+1):
#         if i % j == 0:
#             list1.append(j)
#     a = list1[0:len(list1)-1]
#     if sum(a) == i:
#         perfect.append(i)
#         count += 1
#     list1 = []

# print(perfect,count)


# # Finding the Largest Prime Factor of a Number
# # Difficulty: Medium
# # Topics: Number Theory
# # Description: Write a program to find the largest prime factor of a given number.
# # Example:
# # Input: number = 28
# # Output: 7
# # Explanation: The prime factors of 28 are 2 and 7, with the largest being 7.


# number = int(input("enter a number:"))
# primeno = []
# count = 0
# for i in range(1,number+1):
#     for j in range(1,i+1):
#         if i %j == 0:
#             count +=1
#     if count == 2:
#         primeno.append(i)
#     count = 0

# primefactor = []
# for i in range(0,len(primeno)):
#     if number % primeno[i] == 0:
#         primefactor.append(primeno[i])

# print(max(primefactor))

# # Generating a Matrix of Fibonacci Numbers
# # Difficulty: Medium
# # Topics: Arrays, Matrix Operations
# # Description: Write a program to generate a matrix where each element is a Fibonacci number.
# # Example:
# # Input: size = 3
# # Output:
# # 1 1 2
# # 3 5 8
# # 13 21 34

# import numpy as np
# size = int(input("enter a number:"))
# element = size**2
# fibo = []
# a = 1
# fibo.append(a)
# b = 1
# fibo.append(b)

# for i in range(0,element-2):
#     if a<b:
#         a = a+b
#         fibo.append(a)
#     else:
#         b = b+a
#         fibo.append(b)

# matrixarray = np.arange(1,element+1).reshape(size,size)
# l=0
# for i in range(0,3):
#     j=i+1
#     for k in range(0,3):
#         matrixarray[i:j,k] = fibo[l]
#         l+=1

# print(matrixarray)


# # Finding the Sum of the First N Prime Numbers
# # Difficulty: Medium
# # Topics: Prime Numbers, Mathematical Computations
# # Description: Write a program to calculate the sum of the first N prime numbers.
# # Example:
# # Input: N = 4
# # Output: 17
# # Explanation: The sum of the first 4 prime numbers (2 + 3 + 5 + 7) is 17.

# num = 4
# num1 = num**2
# count = 0
# b = 0
# primeno = []
# for i in range(1,num1+1):
#     if count == num:
#         break
#     for j in range(1,i+1):
#         if i % j == 0:
#             b +=1
#     if b == 2:
#         primeno.append(i)
#         count+=1
#     b = 0

# print(sum(primeno))

# # Checking for a Balanced Bracket Sequence
# # Difficulty: Medium
# # Topics: String Manipulation, Stack
# # Description: Write a program to check if a given string with brackets is balanced.
# # Example:
# # Input: string = "{[()]}"
# # Output: True
# # Explanation: The brackets are balanced.

# str1 = input("enter a char:")
# bracketpair = {"{":"}","[":"]","(":")"}
# loop = len(str1) // 2
# len1 = len(str1)
# count = 0
# for i in range(0,loop):
#     for char in bracketpair.items():
#         if {str1[i],str1[(len1-1)-i]} == set(char):
#             count+=1
# if loop == count:
#     print(True)
# else:
#     print(False)

# # Finding the Sum of Numbers in a String
# # Difficulty: Easy
# # Topics: String Manipulation
# # Description: Write a program to extract and sum all numbers present in a given string.
# # Example:
# # Input: string = "The numbers are 12 and 34"
# # Output: 46
# # Explanation: The sum of numbers 12 and 34 is 46.


str1 = "The numbers are 344 and 341"
list1 = []
number = []
a = ""
for i in range(0,len(str1)+1):
    try:
            list1.append(int(str1[i]))
    except:
        list1.reverse()
        if len(list1) > 1:
            for i in range(0,len(list1)):
                a = str(list1[i]) + a
            number.append(a)
            list1.clear()
            a = ""
a = 0
for i in range(0,len(number)):
    a = int(number[i]) + a

print(a)
























