# Classes and Objects : A class is a blueprint, and an object is an instance of that class.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating an object
my_car = Car("Tesla", "Model S")
my_car.display_info()

# Inheritance : Inheritance allows a class to reuse another class's properties.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_model(self):
        print("Model:", self.model)

my_car = Car("BMW", "X5")
my_car.show_brand()
my_car.show_model()

# Encapsulation : Restrict access to some variables using private variables (__var).
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())  # Works
# print(account.__balance)  Error! Private variable

# Polymorphism : Polymorphism allows methods with the same name in different classes.
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!

#Write a Python program with: A Person class with name and age,A Student class that inherits from Person and has an extra grade attribute, A method to display the student's details.
# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Child class (inherits from Person)
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display_student_info(self):
        self.display_info()  # Call parent class method
        print(f"Grade: {self.grade}")

# Creating an object of Student class
student1 = Student("Asrith", 21, "A")
student1.display_student_info()
