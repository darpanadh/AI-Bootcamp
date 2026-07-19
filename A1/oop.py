# Class and object

# A class car is created with attributes color and brand
class car:
    color = "red"
    brand = "bmw"
    
# An instance of the class car is created i.e car1 which use the attributes of the class car unless it is overridden

car1 = car()
print(car1.color)
print(car1.brand)



# __init__ method 
# It runs automatically when we create an object from a class
class Person:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
        
p1 = Person("Darpan", 20)
print(p1.name)
print(p1.age)