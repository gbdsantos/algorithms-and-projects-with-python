mylist = [1, 2, 3]
myset = set()
type(myset)
type(mylist)

class Dog():
    def __init__(self, breed, name, spots):
        # Attributes
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(mybreed='Huskie', name='Sammy', spots=False)

type(my_dog)

my_dog.breed
my_dog.name
my_dog.spots


