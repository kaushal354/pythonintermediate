#hello world program
print("Hello,World!")

#calculate sum of two numbers enter by the user
num1 = 2
num2 = 3
num = num1 + num2
print(num)

#convert temprature from celsius to fahrenheit
cel = int(input("enter a temp in celcius:"))
fahr = (cel * 9/5 ) + 32
print(fahr)

#area of rectangle
length = 95
width = 96
area = 95 * 96
print(area)

#greeting message
username = input("enter the user name: ")
age = input("enter a age: ")
print("hello,",username,"age:",age,"you are enough do go everthing")

#even and odd
num3 = int(input("enter a number:"))
if num3 % 2 == 0:
    print("even")
else:
    print("odd")

#find a maximum and minimum in a list
list1 = [2,4,6,7,8]
list1.sort()
print(list1[0],list1[4])
#one more method
list2 = [2,9,6,4,3,7,1]
list2.sort()
lstindex = len(list2) - 1
print("min number:",list2[0],"maximum no:",
      list2[lstindex])

#function to check if a string is palindrome
def palindrome():
    string = input("enter a string:")
    lengof = len(string) - 1
    loop2 = lengof / 2
    no = int(loop2)
    string2 = string
    j = 0
    for i in range(0,no):
        if string[i] == string2[lengof - i]:
            j = j + 1
        else:
            j = j + 0
    if j == no:
        print("it is palindrome")
    else:
        print("it is not a palindrome")

palindrome()

#program to find compound interest 
principal = float(input("enter a principal rate:"))
rateofint = float(input("enter a rate of intrest:"))
timeperiod = float(input("enter a timeperiod"))
ci = principal*(1+ (rateofint/100))**timeperiod
print(ci)

#program that converts a given number of days
#into year, week and days
days = int(input("enter a number of days:"))
years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
days_left = remaining_days % 7
print("year:",round(years,2),"week:",round(weeks,2),"days:",round(days_left,2))

#program given a list of integers, find the sum of all +ve number.
list3 = [1,-2,3,5,-3,4,5,-6,-2]
len1 = len(list3) - 1
a = 0
for i in range(0,len1):
    if list3[i] > 0:
        a = a + list3[i]
    else:
        pass

print(a)

#create a program that takes a sentence as input
#and counts the no of words in it
sentence = input("enter a sentence:")
words = sentence.split()
print("the word are there is this sentence",len(words))

#implement a program that swaps the values of two variable
a = 2
b = 4
print(a,b)
c = a+b
b = c - b
a = c - a
print(a,b)

c = 2
d = 4
print(c,d)
d = c + d
c = d - c
b = d - c
print(a,b)



