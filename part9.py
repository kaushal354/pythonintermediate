#create students class that takes name & marks of three subject
#as argument in constructor. then create a method to print a avg.
class students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    @staticmethod
    def hello(): #static method decorator
        print("hello")

    def avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("hi",self.name,"your avg marks is:",sum / 3)

s1 = students("kaushal",[99,98,97])
s1.avg()

s1.name = "iron man"
s1.avg()
s1.hello()

#create a class to represent a basic calcultor with add, sub, multiply, divide methods
class basiccalculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print("the addition of two number is:",self.num1 + self.num2 )

    def sub(self):
        print("the substraction of two number is:",self.num1 - self.num2 )
    
    def mul(self):
        print("the multiplication of two number is:",self.num1 * self.num2)
    
    def div(self):
        print("the division of two number is:",self.num1 / self.num2)

s1 = basiccalculator(25,36)
s1.add()
s1.div()
s1.mul()
s1.sub()


#create a class to represent a book with attributes like title, author and publication year.
class book:
    def __init__(self,title,author,publicationyear):
        self.title = title
        self.author = author
        self.publicationyear = publicationyear

b1 = book("the jungle book","rudiard cipling","1928")
print("title:",b1.title)
print("author:",b1.author)
print("publication year:",b1.publicationyear)

#define a class for circle with methods to calculate its area and circumference
# (pi*r**2,2*pi*r)
import numpy as np
class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        a = np.pi * self.radius ** 2 
        print("the circumference of circle is:",round(a,2))

    def circum(self):
        b = 2*np.pi*self.radius
        print("the area of circle is:",round(b,2))

c1 = circle(3)
c1.circum()
c1.area()



#create a class to represent a student with attributes like name, age, grade
class student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

s1 = student("kaushal",22,90)
print("name:",s1.name,"age:",s1.age,"grade:",s1.grade)

#abstraction revision:-
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

c1 = car()
c1.start()

#create account classs with 2 attributes - balance & account no
#create method for debit, credit & printing the balance

class account:
    def __init__(self,balance,accountno):
        self.balance = balance
        self.account = accountno
    
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance = ",self.balance)

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"Was credited")
        print("total balance = ",self.balance)

    def printbal(self):
        return "the total balance :",self.balance

a1 = account(10000,12345)
print(a1.printbal())
a1.debit(1000)
a1.credit(1000)
a1.credit(100000)
print(a1.printbal)

#Write a Python program that uses a Rectangle class to
#calculate the area and perimeter of a rectangle
class rectangle():
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("the area of rectangle is:",self.length*self.breadth)
    
    def perimeter(self):
        print("the perimeter of rectangle is:",2*(self.length + self.breadth))

rect = rectangle(100,200)
rect.area()
rect.perimeter()

#Create a class to represent a Car with attributes like
# make, model, and year
class car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def displayinfo(self):
        print("the manufacturar of car is:",self.make)
        print("the model of car is:",self.model)
        print("the year of launching of car is:",self.year)

car1 = car("toyta","fortuner",2005)
car1.displayinfo()

#Write a program that uses a Person class to keep track of 
# a person's name, age, and address.
class person:
    name = "kaushal"
    age = 22
    adress = "patna"

p1 = person()
print("the name of person is",p1.name)
print("the age of person is",p1.age)
print("the adress of person is",p1.adress)

# Implement a program that uses a Circle class to calculate 
# the area and circumference of multiple circles
import numpy as np
class circle():
    def __init__(self,count):
            self.count = count
    
    def howmuch(self):
        for i in range(1,self.count+1):
            rad = int(input("enter a radius of circle:"))
            print("area of ",i,"circle:",round(self.area(rad),2))
            print("circumference of ",i,"circle:",round(self.circum(rad),2))

    def area(self,radius):
        a = np.pi * radius ** 2 
        return a

    def circum(self,radius):
        b = 2*np.pi* radius
        return b

c1 = circle(2)
c1.howmuch()

#Create a class to represent a Movie with attributes like 
# title, director, and rating.
class movie:
    def __init__(self,title,director,rating):
        self.title = title
        self.director = director
        self.rating = rating

m1 = movie("Monsters","Anne Sewitsky",7.6)
print("title of movies:",m1.title,"director:", m1.director,"rating:",m1.rating)









