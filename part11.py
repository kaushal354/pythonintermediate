#1. Determining Even/Odd Numbers
# Difficulty: Easy
# Topics: Basic Programming
# Description: Write a program to check whether a number is even or odd.
# Example:
# Input: number = 4
# Output: Even
# Explanation: Since 4 is divisible by 2, it is an even number.

def evenorodd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

n = int(input("number = "))
evenorodd(n)

# 2. Checking for Prime Numbers
# Difficulty: Easy
# Topics: Basic Programming, Number Theory
# Description: Write a program to determine if a number is prime.
# Example:
# Input: number = 7
# Output: Prime
# Explanation: 7 has no divisors other than 1 and itself, so it is a prime number.
def primenos(n):
    a = 0
    for i in range(1,n+1):
        if n % i == 0:
            a = a + 1
        else:
            a = a + 0
    if a == 2:
        print("Prime")
    else:
        print("Not Prime")

n = int(input("number = "))
primenos(n)

#Validating Leap Years
# Difficulty: Easy
# Topics: Basic Programming, Date Handling
# Description: Write a program to check if a given year is a leap year.
# Example:
# Input: year = 2020
# Output: Leap Year
# Explanation: 2020 is divisible by 4 but not by 100, or it is divisible by 400, so it is a leap year.

def leapyear(n):
    if n % 400 == 0:
        print("Leap year")
    elif n% 100 == 0:
        print("not a Leap year")
    elif n % 4 ==0:
        print("Leap year")
    else:
        print("not a Leap year")

n = int(input("year:-"))
leapyear(n)

# Calculating Armstrong Numbers
# Difficulty: Easy
# Topics: Basic Programming, Number Theory
# Description: Write a program to check if a number is an Armstrong number.
# Example:
# Input: number = 153
# Output: Armstrong Number
# Explanation: 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
def armstrongnos(n):
    a = n % 10
    d = n // 10
    b = int(round(d,0) % 10)
    c = d // 10
    if a**3 + b ** 3 + c ** 3 == n:
        print("Armstrong number")
    else:
        print("not a armstrong number")

n = int(input("number:"))
armstrongnos(n)

# Generating the Fibonacci Series
# Difficulty: Easy
# Topics: Basic Programming, Sequences
# Description: Write a program to generate the Fibonacci series up to a given number.
# Example:
# Input: limit = 10
# Output: [0, 1, 1, 2, 3, 5, 8]
# Explanation: The Fibonacci series up to 10 is generated as [0, 1, 1, 2, 3, 5, 8].

def genfibonacci(n):
    a = 0
    print(a,end=" ")
    b = 1
    print(b,end=" ")
    c = 0
    while c < n:
        if a <= b :
            a = a + b
            if a < n:
                print(a,end=" ")
            c = a
        else:
            b = b + a
            if b < n:
                print(b,end=" ")
            c = b

n = int(input("enter a limit:"))
genfibonacci(n)

#Identifying Palindromes
# Difficulty: Easy
# Topics: Basic Programming, String Manipulation
# Description: Write a program to check if a string or number is a palindrome.
# Example:
# Input: string = "radar"
# Output: Palindrome
# Explanation: "radar" reads the same backward as forward.
def palindrome(s):
    string1 = s
    a = len(s) // 2
    j = len(s) - 1
    b = 0
    for i in range(0,a,1):
        if string1[i] == s[j-i]:
            b = b + 1
        else:
            b = b + 0
    if b == a:
        print("Palindrome")
    else:
        print("Not palindrome")

s = input("string=")
palindrome(s)

# Crafting Star Patterns
# Difficulty: Easy
# Topics: Basic Programming, Patterns
# Description: Write a program to create different star patterns (e.g., pyramid, diamond).
# Example:
# Input: patternType = "pyramid", height = 5
# Output:
#       *
#      ***
#     *****
#    *******
#   *********

class pattern:
    def __init__(self,height):
        self.height = height

    def increasingtriangle(self):
        print("increasingtriangle\n")
        for i in range(self.height):
            for j in range(i+1):
                print("*",end=" ")
            print()
    
    def decreasingtriangle(self):
        print("decreasing triangle\n")
        for i in range(self.height):
            for j in range(i,self.height):
                print("*",end=" ")
            print()

    def rightangletriangle(self):
        print("right angle triangle\n")
        for i in range(self.height):
            for j in range(i,self.height):
                print(" ",end= " ")
            for j in range(i+1):
                print("*",end= " ")
            
            print()

    def leftangletriangle(self):
        print("left angle triangle\n")
        for i in range(self.height):
            for j in range(i+1):
                print(" ",end=" ")
            for j in range(i,self.height):
                    print("*",end= " ")
            print()

    def pyramid(self):
        print("pyramid(hill pattern)\n")
        for i in range(self.height):
            for j in range(i,self.height):
                print(" ",end= " ")
            for j in range(i):
                    print("*",end=" ")
            for j in range(i+1):
                        print("*",end= " ")
            print()
    
    def revpyramid(self):
        print("reverse pyramid(rev hill pattern)\n")
        for i in range(self.height):
            for j in range(i+1):
                print(" ",end= " ")
            for j in range(i,self.height-1):
                    print("*",end= " ")
            for j in range(i,self.height):
                        print("*",end= " ")
            print()

    def diamond(self):
        print("diamond pattern \n")
        for i in range(self.height - 1):
            for j in range(i,self.height):
                print(" ",end= " ")
            for j in range(i):
                    print("*",end=" ")
            for j in range(i+1):
                        print("*",end= " ")
            print()
        
        for i in range(self.height):
            for j in range(i+1):
                print(" ",end= " ")
            for j in range(i,self.height-1):
                    print("*",end= " ")
            for j in range(i,self.height):
                        print("*",end= " ")
            print()
                    





pattern1 = pattern(5)
pattern1.increasingtriangle()
pattern1.decreasingtriangle()
pattern1.rightangletriangle()
pattern1.leftangletriangle()
pattern1.pyramid()
pattern1.revpyramid()
pattern1.diamond()

# Finding the Factorial of a Number
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to compute the factorial of a given number.
# Example:
# Input: number = 5
# Output: 120
# Explanation: 5! (factorial) is 5 × 4 × 3 × 2 × 1 = 120.

def fact(n):
    a = 1
    for i in range(n,1,-1):
       a =  i * a
    return a

n = int(input("number:"))
print(fact(n))


# Summing Digits of a Number
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to calculate the sum of digits of a number.
# Example:
# Input: number = 1234
# Output: 10
# Explanation: The sum of the digits 1 + 2 + 3 + 4 = 10.

def sumd(n):
    a = 0
    while n>=10:
        a = (n %10) + a
        n = n // 10
    a = n + a
    return a

n = int(input("number:"))
print(sumd(n))

# Finding the Greatest Common Divisor (GCD)
# Difficulty: Easy
# Topics: Basic Programming, Number Theory
# Description: Write a program to find the GCD of two numbers.
# Example:
# Input: a = 48, b = 18
# Output: 6
# Explanation: The GCD of 48 and 18 is 6.

num1 = int(input("enter a first num:"))
num2 = int(input("enter a 2nd num:"))
x = []
y = []
for i in range(1,num1+1):
    if num1 % i == 0:
        x.append(i)
for i in range(1,num2+1):
    if num2 % i == 0:
        y.append(i)

a = set(x)
b = set(y)
c = max(set.intersection(a,b))
print(c)


# Finding the Least Common Multiple (LCM)
# Difficulty: Easy
# Topics: Basic Programming, Number Theory
# Description: Write a program to find the LCM of two numbers.
# Example:
# Input: a = 12, b = 15
# Output: 60
# Explanation: The LCM of 12 and 15 is 60.

num1 = int(input("enter a 1st number:"))
num2 = int(input("enter a 2nd numbers:"))
i = 2
a = 1
while num1 >1 or num2 > 1:
    if num1 % i == 0 or num2 % i == 0:
            a = i * a
            if num1 % i == 0:
                num1 = num1 / i
            if num2 % i == 0:
                num2 = num2 / i
    else:
        i +=  1

print(a)

# Counting Vowels and Consonants in a String
# Difficulty: Easy
# Topics: Basic Programming, String Manipulation
# Description: Write a program to count vowels and consonants in a given string.
# Example:
# Input: string = "hello world"
# Output: Vowels: 3, Consonants: 7
# Explanation: "hello world" contains 3 vowels (e, o, o) and 7 consonants (h, l, l, w, r, l, d).
str1 = "hello world"
a = "aeiouAEIOU"
b = 0
str1 = str1.replace(" ","")
for i in range(0,len(str1)):
    for j in range(0,len(a)):
        if str1[i] == a[j]:
            b = b + 1
        else:
            b = b + 0
print(f"vowel:{b},cononants:{len(str1) - b}")





