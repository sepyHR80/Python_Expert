class Car:
    def __init__(self):
        self.__speed = 0
    
    def speedUp(self):
        self.__speed += 10
    
    def brake(self):
        self.__speed -= 5
    
    # getter method
    def get_speed(self):
        return self.__speed
    # setter method
    def set_speed(self,speed):
        if speed >= 0 :
            self.__speed = speed

''' 

the speed attribute is encapsulated with private access.
its value is accessed and modified using getter and setter methods.
This encapsulation ensures that the speed attribute is controlled and 
validated, providing a well-defined interface for interacting with 
the Car object while hiding its internal details.

'''


# Usage
car = Car()
'''
if write code like this  : print(car.speed), output is :
AttributeError: 'Car' object has no attribute 'speed'.
'''
car.set_speed(10)
print(car.get_speed()) # output is 10

car.speedUp()
print(car.get_speed()) # output is 20

car.brake()
print(car.get_speed()) # output is 15




