# 1. Basic structure of Inheritance
# -----------------------------------------------------------------------------------------------
class Animal:        # Parent class (Super Class)
    def speak(self):
        print("The animal makes a sound.")

class Hamster(Animal):   # Child class (Sub Class)
    def squeak(self):
        print("Squeak!")

h = Hamster()
h.speak()    # Method inherited from Animal
h.squeak()   # Hamster's own method



# 2. Constructor Overriding and `super()`
# -----------------------------------------------------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor called")

class Hamster(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Call parent constructor
        self.breed = breed

h = Hamster("Hodu", "Golden hamster")
print(h.name, h.breed)

'''
`super().__init()` is a function that calls the constructor of the parent class.
It's not mandatory, but it's a good practice to call it explicitly.
'''



# 3. Method Overriding (Redefinition)
# -----------------------------------------------------------------------------------------------
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow!")

a = Animal()
c = Cat()

a.speak()   # Animal sound
c.speak()   # Meow! (overridden)

'''
A method with the same name can be redefined in the child class.
'''



# 4. Multiple Inheritance
# -----------------------------------------------------------------------------------------------
class Flyable:
    def fly(self):
        print("Can fly")

class Bird(Animal, Flyable):   # Inherits from both Animal and Flyable
    pass

b = Bird("Sparrow")
b.speak()        # Inherited from Animal
b.fly()          # Inherited from Nocturnal

'''
Python supports multiple inheritance, but clear separation of responsibilities is important.
'''



# 5. `isinstance` and `issubclass`
# -----------------------------------------------------------------------------------------------





# 6. 
# -----------------------------------------------------------------------------------------------





# 7. 
# -----------------------------------------------------------------------------------------------





# 8. 
# -----------------------------------------------------------------------------------------------



