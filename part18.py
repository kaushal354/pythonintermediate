#Generating a Right-Angle Triangle Pattern of Numbers
# Difficulty: Easy
# Topics: Patterns
# Description: Write a program to create a right-angle triangle pattern with numbers.
# Example:
# Input: height = 4
# Output:
# 1
# 12
# 123
# 1234
height = int(input("enter a number:"))
for i in range(height):
    for j in range(i+1):
        print(j+1,end = " ")
    print()


# Finding All Divisors of the Product of Two Numbers
# Difficulty: Medium
# Topics: Number Theory
# Description: Write a program to find all divisors of the product of two given numbers.
# Example:
# Input: number1 = 6, number2 = 10
# Output: [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
# Explanation: The product of 6 and 10 is 60, and its divisors are listed.
num1 = int(input("enter a first number:"))
num2 = int(input("enter a 2nd number:"))
product = num1 * num2
div = []
for i in range(1,product+1):
    if product % i == 0:
        div.append(i)

print(div)




# Finding the Longest Sequence of Consecutive 1s in a Binary Array
# Difficulty: Medium
# Topics: Arrays, Binary Operations
# Description: Write a program to find the longest sequence of consecutive 1s in a binary array.
# Example:
# Input: array = [1, 1, 0, 1, 1, 1]
# Output: 3
# Explanation: The longest sequence of 1s is [1, 1, 1] with length 3.
array = [1,1,0,1,1,1]
onesbinard = []
count = 0
for i in array:
    if i == 1:
        count+=1
    else:
        onesbinard.append(count)
        count = 0
onesbinard.append(count)
print(max(onesbinard))

# Calculating the Sum of the First N Fibonacci Numbers
# Difficulty: Medium
# Topics: Fibonacci Sequence, Mathematical Computations
# Description: Write a program to calculate the sum of the first N Fibonacci numbers.
# Example:
# Input: N = 5
# Output: 12
# Explanation: The first 5 Fibonacci numbers are 1, 1, 2, 3, 5, and their sum is 12.
num = int(input("enter a range:"))
a = 0
b = 1
fibonnum = []
fibonnum.append(a)
fibonnum.append(b)
for i in range(1,num):
    if a<b:
        a = a +b
        fibonnum.append(a)
    else:
        b = a + b
        fibonnum.append(b)
print(sum(fibonnum))



# Checking for a Repeated Substring in a String
# Difficulty: Medium
# Topics: String Manipulation
# Description: Write a program to check if a substring is repeated within a given string.
# Example:
# Input: string = "abab"
# Output: True
# Explanation: The substring "ab" is repeated.
string = "abab"
a = 2
#finding the substr
substr = []
for i in range(0,len(string)):
    l = a
    l = 2
    for j in range(l,len(string)+1):
        if string[i:j] != "":
            if len(string[i:j]) >= 2:
                substr.append(string[i:j])
                l+=1
    a+=1
#common substr in the substr
count = 0
l = 2
repstr = []
for i in range(0,len(substr)):
    for j in range(0,len(substr)):
        if substr[i] == substr[j]:
            count+=1
    if count >= l:
        repstr.append(substr[i])
        l = count
        count = 0
    count = 0
a = 0

#maxlen of a common substr
maxlen = []
for i in range(0,len(repstr)):
    a = repstr[i]
    b = len(a)
    maxlen.append(b)
maxlen = max(maxlen)

#finding the repeated substr
repstr1 = []
for i in range(0,len(repstr)):
    if len(repstr[i])==maxlen:
        repstr1.append(repstr[i])

print(repstr1)

# Finding the Number of Words in a String
# Difficulty: Easy
# Topics: String Manipulation
# Description: Write a program to count the number of words in a given string.
# Example:
# Input: string = "Hello world"
# Output: 2
# Explanation: There are 2 words in the string.
string = "Hello world"
word = string.split()
print(len(word))

# Finding the Median of a List of Numbers
# Difficulty: Medium
# Topics: Sorting, Mathematical Computations
# Description: Write a program to find the median value of a list of numbers.
# Example:
# Input: list = [3, 1, 4, 1, 5]
# Output: 3
# Explanation: After sorting the list to [1, 1, 3, 4, 5], the median is 3.
list1 = [3,1,4,1,5]
list1.sort()
print(list1)
if len(list1) % 2 ==0:
    med = len(list1) // 2
    print(list1[med-1],list1[med])
else:
    med = len(list1)//2
    print(list1[med])



# Generating a Matrix with a Diagonal Pattern
# Difficulty: Medium
# Topics: Matrix Operations
# Description: Write a program to create a matrix where elements form diagonal lines of a given pattern.
# Example:
# Input: size = 4
# Output:
# 1 0 0 0
# 1 1 0 0
# 1 1 1 0
# 1 1 1 1
import numpy as np
size = int(input("enter a size of array:"))
array = np.zeros((size,size),dtype=int)
array1= np.arange(1,(size**2)+1).reshape(size,size)
for i in range(0,size):
        j = i+1
        for k in range(0,size):
            if k < j:
                array[i:j,k] = 1
            else:
                array[i:j,k] = 0
print(array)

# Finding the Sum of the First N Even Numbers
# Difficulty: Easy
# Topics: Mathematical Computations
# Description: Write a program to calculate the sum of the first N even numbers.
# Example:
# Input: N = 4
# Output: 20
# Explanation: The first 4 even numbers are 2, 4, 6, 8, and their sum is 20.

num = int(input("enter a number:"))
count = 0
a = 0
i = 1
while count<4:
        if i %2 == 0:
            count+=1
            a = a + i
            i+=1
        i+=1
print(a)




# Finding the Count of Digits Greater Than a Specific Value
# Difficulty: Easy
# Topics: Mathematical Computations
# Description: Write a program to count how many digits in a number are greater than a specific value.
# Example:
# Input: number = 54321, value = 3
# Output: 2
# Explanation: The digits
# greater than 3 in 54321 are 5, 4, so the count is 2.

number = int(input("enter a number:"))
value = int(input("enter a value:"))
grnum = []
while number>0:
    a = number % 10
    if a > value:
        grnum.append(a)
    number = number // 10
print(grnum)
print(len(grnum))



# Generating a Pattern of Prime Numbers
# Difficulty: Medium
# Topics: Prime Numbers, Patterns
# Description: Write a program to generate a pattern where each row contains the first few prime numbers.
# Example:
# Input: rows = 3
# Output:
# 2
# 2 3
# 2 3 5
rows = int(input("enter a number:"))
primeno = []
count = 0
pcount = 0
i = 2
while count < rows:
    for j in range(1,i+1):
        if i % j == 0:
            pcount +=1
    if pcount == 2:
        primeno.append(i)
        i+=1
        count+=1
    else:
        i+=1
    pcount = 0

for i in range(rows):
    for j in range(0,i+1):
        print(primeno[j],end = " ")
    print()





# Finding the Common Elements in Two Arrays
# Difficulty: Medium
# Topics: Arrays
# Description: Write a program to find common elements between two arrays.
# Example:
# Input: array1 = [1, 2, 3, 4], array2 = [3, 4, 5, 6]
# Output: [3, 4]
# Explanation: The common elements between the two arrays are 3 and 4.
array1 = [1,2,3,4]
array2= [3,4,5,6]
array1 = set(array1)
array2 = set(array2)
print((array1).intersection(array2))

# Finding the Sum of the Squares of All Even Numbers Up to N
# Difficulty: Medium
# Topics: Mathematical Computations
# Description: Write a program to calculate the sum of squares of all even numbers up to a given N.
# Example:
# Input: N = 4
# Output: 20
# Explanation: The even numbers up to 4 are 2 and 4, and their squares are 4 and 16. The sum is 20.

num = int(input("enter a number:"))
a = 0
sum = 0
for i in range(1,num+1):
    if i %2 == 0:
        a = i**2
        sum = a + sum
print(sum)

