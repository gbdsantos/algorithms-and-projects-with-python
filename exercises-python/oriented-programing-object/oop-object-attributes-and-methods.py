class Dog():

    species = 'mammal'

    def __init__(self, breed, name):
        # Attributes
        self.breed = breed
        self.name = name

    # OPERATIONS/Actions ----> Methods
    def bark(self, number):
        print('WOOF! My name is{} and the number is {}'.format(self.name, number))

my_dog = Dog('Lab', 'Frankie')

type(my_dog)

# Atributes
my_dog.breed
my_dog.name
my_dog.species

# Method
my_dog.bark()
my_dog.bark(10)

class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle()
my_circle.pi
my_circle.radius

my_circle.get_circumference()




