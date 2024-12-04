#Problem 1: Print a Right-Angle Triangle of Stars
# Difficulty: Easy
# Topics: Pattern Printing
# Hint: Print a right-angle triangle pattern of stars (*). 
# Each row should contain an increasing number of stars, starting from 1 star in the first row.
# Example 1: Input: n = 4
# Output:
# *
# **
# ***
# ****

num = int(input("enter a number:"))
for i in range(num):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

# Problem 2: Print a Square of Stars
# Difficulty: Easy
# Topics: Pattern Printing
# Hint: Print a square pattern of stars (*). 
# Each row and column should have the same number of stars.
# Example 1: Input: n = 5
# Output:
# *****
# *****
# *****
# *****
# *****

num = int(input("enter a number:"))
for i in range(0,num):
    for j in range(0,num):
        print("*",end=" ")
    print()

# Problem 3: Print a Pyramid Pattern
# Difficulty: Easy
# Topics: Pattern Printing
# Hint: Print a pyramid pattern with stars (*). 
# The pyramid should have a single peak and each row should have an increasing number of stars, centered horizontally.
# Example 1: Input: n = 3
# Output:
#   *
#  ***
# *****
num = int(input("enter a number:"))
for i in range(num):
    for j in range(i,num):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()


# Problem 4: Print a Diamond Pattern
# Difficulty: Easy
# Topics: Pattern Printing
# Hint: Print a diamond pattern with stars (*).
# The pattern should include a single peak in the middle with symmetric rows above and below it.
# Example 1: Input: n = 3
# Output:
#   *
#  ***
# *****
#  ***
#   *
num = int(input("enter a number:-"))
for i in range(num - 1):
    for j in range(i,num):
        print(" ",end= " ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end= " ")
    print()
for i in range(num):
    for j in range(i+1):
        print(" ",end= " ")
    for j in range(i,num-1):
        print("*",end= " ")
    for j in range(i,num):
        print("*",end= " ")
    print()


# Crafting Star Patterns
# Difficulty: Easy
# Topics: Basic Programming, Patterns
# Description: Write a program to create different star patterns (e.g., pyramid, diamond).
# Example:
# Input: patternType = "pyramid", height = 5
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

    def rightsided(self):
        print("right sided triangle")
        for i in range(self.height):
            for j in range(i+1):
                print(" ",end=" ")
            for j in range(i,self.height):
                print("*",end=" ")
            print()

height = int(input("enter a height:"))
pat = pattern(height)
pat.diamond()
pat.decreasingtriangle()
pat.increasingtriangle()
pat.pyramid()
pat.revpyramid()
pat.rightangletriangle()
pat.rightsided()


# Problem 5: Print a Hollow Square of Stars
# Difficulty: Easy
# Topics: Pattern Printing
# Hint: Print a hollow square pattern with stars (*).
# The border of the square should be filled with stars while the inner part should be empty.
# Example 1: Input: n = 5
# Output:
# *****
# *   *
# *   *
# *   *
# *****

num = int(input("enter a number:"))
for i in range(num):
    for j in range(num):
        if(i==0):
            print("*",end=" ")
        elif(i==num-1):
            print("*",end=" ")
        else:
            if(j==0):
                print("*",end=" ")
            elif(j==num-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()


# Problem 6: Print a Number Triangle
# Difficulty: Easy
# Topics: Pattern Printing
# Hint: Print a right-angle triangle pattern with numbers.
# Each row should contain an increasing sequence of numbers starting from 1.
# Example 1: Input: n = 4
# Output:
# 1
# 12
# 123
# 1234
num = int(input("enter a number:"))
for i in range(num):
    for j in range(i+1):
        print(j+1,end=" ")
    print()


# Problem 7: Print an Inverted Triangle Pattern
# Difficulty: Easy
# Topics: Pattern Printing
# Hint: Print an inverted triangle pattern with stars (*).
# Each row should contain decreasing numbers of stars from the top row.
# Example 1: Input: n = 5
# Output:
# *****
#  ****
#   ***
#    **
#     *
num = int(input("enter a number:"))
for i in range(num):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(num-i):
        print("*",end=" ")
    print()

# Problem 8: Print a Diamond Pattern with Numbers
# Difficulty: Easy
# Topics: Pattern Printing
# Hint: Print a diamond pattern with numbers.
# The pattern should have a peak in the middle with symmetric rows above and below it.
# Example 1: Input: n = 3
# Output:
#   1
#  121
# 12321
#  121
#   1
num = int(input("enter a number"))
for i in range(num - 1):
    for j in range(i,num):
        print(" ",end= " ")
    for j in range(i):
        print(j+1,end=" ")
    for j in range(i+1):
        print((i+1)-j,end= " ")
    print()
for i in range(num):
    for j in range(i+1):
        print(" ",end= " ")
    for j in range(i,num-1):
        print((j+1)-i,end=" ")
        k = j+1
    for j in range(i,num):
        print((k+1)-j,end=" ")
    print()


# Problem 9: Print a Right-Angle Triangle of Numbers
# Difficulty: Easy
# Topics: Pattern Printing
# Hint: Print a right-angle triangle pattern with increasing numbers.
# Each row should contain a continuous sequence of increasing numbers.
# Example 1: Input: n = 4
# Output:
# 1
# 23
# 456
# 78910
num = int(input("enter a number:"))
k=1
for i in range(num):
    for j in range(i+1):
        print(k,end=" ")
        k=k+1
    print()



# Problem 10: Print a Pyramid Pattern with Numbers
# Difficulty: Easy
# Topics: Pattern Printing
# Hint: Print a pyramid pattern with increasing numbers.
# Each row should have an increasing sequence of numbers, centered horizontally.
# Example 1: Input: n = 3
# Output:
#   1
#  232
# 34543
num = int(input("enter a number:"))
for i in range(num):
    for j in range(i,num):
        print(" ",end=" ")
    for j in range(i+1):
        print(j+(i+1),end=" ")
        k = j+(i)
    for j in range(i):
        print((k)-j,end=" ")
    print()

