"""
# some practice
class Square:
    def __int__(self, height = "0", width = "0"):
        self.height = height
        self.width = width
    
    @property
    def height(self):
        print("Rethrivng the height")
        return self.__height
    @property
    def width(self):
        print("Retriving the width")
        return self.__width
    
    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter number for width")
    
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter number for height")


    def get_area(self):
        return int(self.__width)*int(self.__height)

def main():
    square = Square()
    height = input("Enter Height: ")
    width = input("Enter width: ")
    square.height = height
    square.width = width
    print("Height: ",square.height)
    print("Widht: ", square.width)
    print("The area is: ", square.get_area())

main()

"""
# OOP Exercise 1: Create a Class with instance attributes
"""
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelx = Vehicle(240, 18)
print(modelx.max_speed, modelx.mileage)

"""

# OOP Exercise 2: Create a Vehicle class without any variables and methods

"""class Vehicle:
    pass
"""
# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

"""class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
"""

# OOP Exercise 4: Class Inheritance
"""
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers. Max speed {self.max_speed}"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    
School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())

"""
# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
"""
class Vehicle:
    #class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mieage:", School_bus.mileage)

car = Car("Audi", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

"""
# OOP Exercise 6: Class Inheritance

"""class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount
    
School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
"""

# OOP Exercise 7: Check type of an object

"""class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))
"""
# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(isinstance(School_bus, Vehicle))