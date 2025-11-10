#object oriented programming concepts
#classes and objects
#methods and attributes
#structural programming
#maintain 
#debug /error searching
#reuseable code.


class Saad:
    name = "Saad Qadri" #attribute


obj = Saad() #object
print(obj.name) #accessing attribute


class Person:
    def __init__(self, name, age): #constructor method
        self.name = name  #attribute
        self.age = age    #attribute



obj2 = Person("Muhammad Saad", 25) #object
print("Name:", obj2.name)
print("Age:", obj2.age)




class Rectangle:
    def __init__(self, width, height): #constructor method
        self.width = width  #attribute
        self.height = height #attribute

    def area(self):  #method
        return self.width * self.height

    def perimeter(self): #method
        return 2 * (self.width + self.height)

rect = Rectangle(5, 10) #object
print("Area:", rect.perimeter()) #calling method



class Car:
    def __init__(self, model, price): #constructor method
        self.model = model #attribute
        self.price = price #attribute

class Salesman(Car):
    def __init__(self, name): #constructor method
        self.name = name #attribute
        self.total_sales = 0 #attribute
        self.cars_sold = 0 #attribute
    
    def sell_car(self, car, discoun=0): #method
        final_price = car.price - (car.price * discoun / 100)
        self.total_sales += final_price
        self.cars_sold += 1
        print(f"{self.name} sold {car.model} for ${final_price}")
    
    def weekly_commission(self): #method
        if self.cars_sold >= 5:
            return 1500
        else:
            return 500
        
    def monthly_summary(self): #method
        avr_per_week = self.cars_sold / 4
        target = 20
        print(f"Monthly Summary for {self.name}:")
        print(f"Total Cars Sold: {self.cars_sold}")
        print(f"Total Sales: ${self.total_sales}")
        print(f"Average Cars Sold per Week: {avr_per_week}")
        if self.cars_sold >= target:
            print("Target Achieved!")
        else:
            print(f"Target Remianing{target - self.cars_sold}")
        print(f"Total Commission Earned: ${self.weekly_commission() * 4}")



car1 = Car("Toyota Camry", 36000)
car2 = Car("Honda Accord", 30000)
car3 = Car("Ford Mustang", 55000)
car4 = Car("Chevrolet Malibu", 28000)
car5 = Car("Nissan Altima", 32000)  
car6 = Car("BMW 3 Series", 45000)

salesman = Salesman("Saad Qadri")
salesman.sell_car(car1)
salesman.sell_car(car2)
salesman.sell_car(car3)
salesman.sell_car(car4)
salesman.sell_car(car5)
salesman.sell_car(car6)

salesman.monthly_summary()


#Inheritence
class Animal:
    def speak(self): #parent class method
        return "Animal speaks"  

class Dog(Animal): #child class inheriting from Animal
    def speak(self):
        return "Woof!"


#polymorphism, smae method name but different behavior
class Logistic:
    def __init__(self, vehiclesbrand, model):
        self.vehiclesbrand = vehiclesbrand
        self.model = model
    def move(self):
        print("Logistic vehicle is moving")


class Truck:
    def __init__(self, vehiclesbrand, model):
        self.vehiclesbrand = vehiclesbrand
        self.model = model
    def move(self):
        print("Logistic Truck is moving")
class Ship:
    def __init__(self, vehiclesbrand, model):
        self.vehiclesbrand = vehiclesbrand
        self.model = model
    def move(self):
        print("Logistic Ship is sailing")

class Plane:
    def __init__(self, vehiclesbrand, model):
        self.vehiclesbrand = vehiclesbrand
        self.model = model
    def move(self):
        print("Logistic Plane is flying")

#python encapsulation

#inside the class we have to protect data
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  #private attribute
        self.__balance = balance  #private attribute

    def deposit(self, amount):  #public method
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):  #public method
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid amount")

    def get_balance(self):  #public method
        return self.__balance
    
    def _get_account_number(self):  #protected method
        return self.__account_number
