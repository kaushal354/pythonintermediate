#imaginary function(polymorphism)
class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2):
        newReal = self.real + num2.real
        newimg = self.img + num2.img
        return complex(newReal,newimg)

num1 = complex(1,3)
num1.showNumber()

num2 = complex(4,6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

#define a employee class with attributes role,deptartment,
#&salary. this class also has a show detailes method
#create an enigineer class that inherits property
#from employee & has additional attributes :name & age

class employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetailes(self):
        print("salary: ",self.salary)
        print("dept: ",self.dept)
        print("role: ",self.role)

class engineer(employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75000")

c1 = employee("accountant","finance","60000")
c1.showdetailes()

engg1 = engineer("elonmusk","40")
engg1.showdetailes()

#create a class called order which store item & its price.
#use dunder function __gt__() to convey that:
#order1>order2 if price of order1>price of order2

class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    
    def __gt__(self,c2):
        return self.price > c2.price

c1 = order("tea",96)
c2 = order("chips",100)

print(c1>c2)

#create a base class animal with a method sound()
#and create derived classes dog and cat with their
#own sound.
class animal:
    def sound(self):
        print("this animal makes a sound")

class dog(animal):
    def sound(self):
        print("The dog barks")

class cat(animal):
    def sound(self):
        print("the cat meows")

Animal = animal()
Dog = dog()
Cat = cat()

Animal.sound()
Dog.sound()
Cat.sound()

#implement a class hierchy to represent different type
#of vehicle (car,bike) with their own attribute and methods
class vehicle:
    def vehtype(self):
        print("the viechle is ")

class car(vehicle):
    def __init__(self,milage):
        self.milage = milage

    def fulebymilage(self,fuel):
        fulebymilage = fuel * self.milage
        return "the fuel milage of car:",fulebymilage

class bike(vehicle):
    def __init__(self,milage):
        self.milage = milage

    def fulebymilage(self,fuel):
        fulebymilage = fuel * self.milage
        return "the fuel milage of bike:",fulebymilage

veh = vehicle()
car2 = car(25)
bike1 = bike(78)
veh.vehtype()
print(car2.fulebymilage(3))
print(bike1.fulebymilage(5))


#create a class person with private attributes and
#define method to get and set the values of those
#attributes.
class person:
    def __init__(self,age,mobileno):
        self.__age = age
        self.__mobileno = mobileno

    def getage(self):
        return self.__age
    
    def setage(self,age):
        if age > 0 :
            print(age)
        else:
            print("please enter a valid age")

    def getmobileno(self):
        return self.__mobileno
    
    def setmobileno(self,mobileno):
        if len(mobileno) == 10:
            print(mobileno)
        else:
            print("enter a valid mobile no")

c1 = person(25,96613)
print("the person private age is:",c1.getage(),"the person private phone no",c1.getmobileno())
c1.setmobileno("9661392401")
c1.setage(23)

#Create a base class Shape with methods to calculate area
# and perimeter, and derive classes Circle and Square
import numpy as np
class shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        area1 = np.pi * self.radius **2
        print(round(area1,2))
    
    def perimeter(self):
        perimeter2 = 2*np.pi*self.radius
        print(round(perimeter2,2))

class square(shape):
    def __init__(self,sides):
        self.sides = sides

    def area(self):
        area1 = self.sides **2
        print(round(area1,2))
    
    def perimeter(self):
        perimeter2 = 4 * self.sides
        print(round(perimeter2,2))

c1 = circle(5)
s1 = square(6)
c1.area()
c1.perimeter()
s1.perimeter()
s1.area()

Implement a class hierarchy to represent different types 
of employees (Manager, Engineer) with their attributes
class employees:
    def __init__(self,name,post,salary):
        self.name = name
        self.post = post
        self.salary = salary

    def employeesinfo(self):
        print("the name of emp:",self.name)
        print("the post of employee:",self.post)
        print("the salary of employee is:",self.salary)

class manager(employees):
    def __init__(self,name,post,salary,teamsize,bonus):
        super().__init__(name, post, salary)
        self.teamsize = teamsize
        self.bonus = bonus

    def managerinfo(self):
        self.employeesinfo()
        print("the team size of manager is:",self.teamsize)
        print("the bonus of manager is:",self.bonus)

class engineer(employees):
    def __init__(self, name, post, salary,skill,project):
        super().__init__(name, post, salary)
        self.skill = skill
        self.project = project

    def engineerinfo(self):
        self.employeesinfo()
        print("the skill of engineer is:",self.skill)
        print("the project done by engg:",self.project)

E1 = engineer("kaushal","engineer1",9000,["java","c","python"],"machine learning")
M1 = manager("abhishek","manager",10100,90,2500)

print("the engineer detailes is:\n")
E1.engineerinfo()
print("the manager info:\n")
M1.managerinfo()

# Write a Python program that uses inheritance to
# represent a hierarchy of shapes (Triangle, Rectangle,
# etc.
import numpy as np
class shape:
    def __init__(self,length,width,height,base,side,radius,diagonal):
        self.length = length
        self.width = width
        self.height = height
        self.base = base
        self.side = side
        self.radius = radius
        self.diagonal = diagonal

    def infoshape(self):
        print("the length of shape is:",self.length)
        print("the width of shape is:",self.width)
        print("the height of shape is:",self.height)
        print("the base of shape is:",self.base)
        print("the side of shape is:",self.side)
        print("the radius of shape is:",self.radius)
        print("the diagonal of shape is:",self.diagonal)

class rectangle(shape):
    def __init__(self, length, width, height, base, side, radius, diagonal):
        super().__init__(length, width, height, base, side, radius, diagonal)

    def area(self):
        area = self.length * self.width
        print("the area of rectangle",area)

    def perim(self):
        perim = 2*(self.length + self.width)
        print("the area of rectangle",perim)

class triangle(shape):
    def __init__(self, length, width, height, base, side, radius, diagonal,side2,side3):
        super().__init__(length, width, height, base, side, radius, diagonal)
        self.side2 = side2
        self.side3 = side3

    def area(self):
        area = 0.5 * self.base*self.height
        print("the area of traingle:",area)

    def perim(self):
        perim = self.side + self.side2 + self.side3
        print("the perimeter of triangle is:",perim)

class circle(shape):
    def __init__(self, length, width, height, base, side, radius, diagonal):
        super().__init__(length, width, height, base, side, radius, diagonal)
    
    def area(self):
        area = np.pi * (self.radius **2)
        print("the area of circle is:",area)
    
    def perim(self):
        perim = 2*np.pi*self.radius
        print("the perimeter of circle is:",perim)

class rhombus(shape):
    def __init__(self, length, width, height, base, side, radius, diagonal,diagonal2):
        super().__init__(length, width, height, base, side, radius, diagonal)
        self.diagonal2 = diagonal2

    def area(self):
        area = 0.5 * self.diagonal * self.diagonal2
        print("the area of rhombus",area)
    
    def perim(self):
        perim = 4 * self.side
        print("the perimeter of rhombus is:",perim)


r1 = rectangle(24,26,3,5,7,4,5)
r1.area()
r1.perim()

t1 = triangle(24,26,6,4,3,4,2,5,6)
t1.area()
t1.perim()

c1 = circle(24,26,24,56,4,8,62)
c1.perim()
c1.area()

r2 = rhombus(24,26,4,57,25,82,5,5)
r2.area()
r2.perim()


# Create a class hierarchy to represent different types of 
# animals (Bird, Fish) with their own attributes and 
# methods
class animals:
    def __init__(self,origin):
        self.origin = origin

    def animalinfo(self):
        print("the animal belong to the:",self.origin)

class birds(animals):
    def __init__(self,origin,name,altitude):
        super().__init__(origin)
        self.name = name
        self.altitude = altitude
    
    def birdinfo(self):
        print("the bird origin is:",self.origin)
        print("the bird name is:",self.name)
        print("the bird flew in the altitude of:",self.altitude)
    
class fish(animals):
    def __init__(self, origin,name,deepofsea):
        super().__init__(origin)
        self.name = name
        self.deepofsea = deepofsea
    
    def fishinfo(self):
        print("the fish origin is:",self.origin)
        print("the fish name is:",self.name)
        print("the bird down in the altitude of:",self.deepofsea)

a2 = animals("japan")
b2 = birds("india","tummy",50000)
f2 = fish("india","dummy",10000)

a2.animalinfo()
b2.birdinfo()
f2.fishinfo()

# Implement a program that uses inheritance to represent a 
# hierarchy of vehicles (Car, Bike, Truck, etc.)
class vehicles:
    def __init__(self,weight,purpose,type):
        self.weight = weight
        self.purpose = purpose
        self.type = type
    
    def vehicleinfo(self):
        print("the veichle weight is:",self.weight)
        print("the vehicle type is:",self.type)
        print("the vehicle purpose",self.purpose)

class car(vehicles):
    def __init__(self, weight, purpose, type,seatcapicity,maxspeed,model):
        super().__init__(weight, purpose, type)
        self.seatcapicity = seatcapicity
        self.maxspeed = maxspeed
        self.model = model
    
    def carinfo(self):
        print("the weight of car is:",self.weight)
        print("the car purpose is:",self.purpose)
        print("the car type is:",self.type)
        print("the car seating capaicity is:",self.seatcapicity)
        print("the car max speed is:",self.maxspeed)
        print("the car model is:",self.model)
    
class bike(vehicles):
    def __init__(self, weight, purpose, type,seatcapicity,maxspeed,model):
        super().__init__(weight, purpose, type)
        self.seatcapicity = seatcapicity
        self.maxspeed = maxspeed
        self.model = model
    
    def bikeinfo(self):
        print("the weight of bike is:",self.weight)
        print("the bike purpose is:",self.purpose)
        print("the bike type is:",self.type)
        print("the bike seating capaicity is:",self.seatcapicity)
        print("the bike max speed is:",self.maxspeed)
        print("the bike model is:",self.model)

class Truck(vehicles):
    def __init__(self, weight, purpose, type,seatcapicity,maxspeed,model,load):
        super().__init__(weight, purpose, type)
        self.seatcapicity = seatcapicity
        self.maxspeed = maxspeed
        self.model = model
        self.load = load
    
    def truckinfo(self):
        print("the weight of truck is:",self.weight)
        print("the truck purpose is:",self.purpose)
        print("the truck type is:",self.type)
        print("the truck seating capaicity is:",self.seatcapicity)
        print("the truck max speed is:",self.maxspeed)
        print("the truck model is:",self.model)
        print("the truck max load is:",self.load)

v1 = vehicles(98,"passenger","diesel")
c1 = car(100,"passenger","petrol",5,140,"tata nova")
b2 = bike(39,"passenger","petrol",2,110,"dreamneo")
t1 = Truck(39,"goods","diseal",2,70,"tata vina","90 ton")

v1.vehicleinfo()
c1.carinfo()
b2.bikeinfo()
t1.truckinfo()


# Write a Python program that uses encapsulation to 
# protect sensitive information in a User class.
class user:
    def __init__(self,name,password):
        self.name = name
        self.__password = password

    def genpass(self):
        return self.__password

c1 = user("kaushal",957260)
print(c1.genpass())

#Create a class hierarchy to represent different types of 
# electronics (Phone, Laptop) with their attributes

class electronic:
    def __init__(self,camera,processor,ram,hdd,gpu,os):
        self.camera = camera
        self.processor = processor
        self.ram = ram
        self.hdd = hdd
        self.gpu = gpu
        self.os = os
    
    def deviceinfo(self):
        print("the camera megapixel is:",self.camera)
        print("the processor is of:",self.processor)
        print("the ram is of:",self.ram)
        print("the harddisk capacity:",self.hdd)
        print("the gpu capacity is:",self.gpu)
        print("the os support is:",self.os)

class phone(electronic):
    def __init__(self, camera, processor, ram, hdd, gpu, os,displaysize):
        super().__init__(camera, processor, ram, hdd, gpu, os)
        self.displaysize = displaysize

    def phoneinfo(self):
        print("the phone camera megapixel is:",self.camera)
        print("the processor is of:",self.processor)
        print("the ram is of:",self.ram)
        print("the harddisk capacity:",self.hdd)
        print("the gpu capacity is:",self.gpu)
        print("the os support is:",self.os)
        print("the display size is:",self.displaysize)
        
class laptop(electronic):
    def __init__(self, camera, processor, ram, hdd, gpu, os,displaysize):
        super().__init__(camera, processor, ram, hdd, gpu, os)
        self.displaysize = displaysize

    def laptopinfo(self):
        print("the laptop camera megapixel is:",self.camera)
        print("the processor is of:",self.processor)
        print("the ram is of:",self.ram)
        print("the harddisk capacity:",self.hdd)
        print("the gpu capacity is:",self.gpu)
        print("the os support is:",self.os)
        print("the display size is:",self.displaysize)

d1 = electronic(48,"snapdragon",32,"500","nvidia","microsoft window")
p1 = phone(48,"snapdragon",32,"500","nvidia","andiroid 14",6.67)
l1 = laptop(0.3,"intel",64,"1tb","nvidia","windows",15.6)

d1.deviceinfo()
p1.phoneinfo()
l1.laptopinfo()






