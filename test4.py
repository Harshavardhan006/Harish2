def twoSum( nums, target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
nums=[2,7,11,15]
target=9
print(twoSum(nums,target)) 

'''oops vs procedural 

OOPS-Object Oriented Programming System 1.It will deal with Object only
                                        2.It can be easily maintain 
                                        3.It comes under real world entities it can be easily understand
                                        4.Data hiding-secure and Data access

Procedural Oriented 1.Step by step instruction
                    2.Longer programs so can't maintain
                    3.no real entities 
                    4.data binding 

concepts on oops:
Classes and objects
constructor
Inheritance
Polymorphism
Encapsulation,Data Abstraction

Classes and Objects:
#Syntax
class Person():
#class with print
class Person():
    print("hiii")

class Person():
    print("hiii")
print(person()) 

#class with variable
class Person():
    print("hiii")
    a=10
    print(a)


Examples:
class student():
    def __init__(self,name,register):
        self.name=name
        self.register=register
    def display(self):
        print("name",self.name)
        print("register no",self.register)
s1=student("harish","50")
print(s1.name)
print(s1.register)
s1.display

class fruit():
    def __init__(self,color):
        self.color="black"
apple=fruit("red")
print(apple.color)            
class teacher():
    def __init__(self,name,reg):
        self.name=name
        self.reg=reg
    def display(self):
        print("name:",self.name)
        print("Reg no",self.reg)
t1=teacher("thomas","1")
t2=teacher("john","2")
t1.display()
t2.display()  


class empolyee1():
    def info(self):
        name="harish"
        age=22
        print("name:",name)
        print("age:",age)
class empolyee2():

    def info(self):
        name="naveen"
        age=22
        print("name:",name)
        print("age:",age)
o1=empolyee1()
o2=empolyee2()
o2.info()
o1.info()


import math
class Shape():
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self,name,r):
        super().__init__(name)
        self.r=r
    def area(self):
        print(math.pi*self.r**2)
    def perimeter(self):
        print(2*math.pi*self.r)
class square(shape):
    def __init__(self,name,a):
        super().__init__(name)
        self.a=a
    def area(self):
        print(self.a**2)
    def perimeter(self):
        print(4*self.a)
c1=circle("circle",4)
s1=square("square",4)
c1.area()
c1.perimeter()
s1.area()
s1.perimeter()

class car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("drive")
class boat(car):
    def __init__(self,brand,model):
        super().__init__(brand,model)
    def move(self):
        print("sail")
class plane(car):
    def __init__(self,brand,model):
        super().__init__(brand,model)
    def move(self):
        print("fly")
car1=car("bmw","007")
boat1=boat("bond","007")
plane1=plane("emirates","ed07")


for x in (car1,boat1,plane1):
    print(x.brand)
    x.move()  '''
















    

             





