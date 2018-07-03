from collections import namedtuple

t = (1, 2, 3)
t[0]

#Using namedtuple
Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='Lab',name='Sammy')

sam

sam.age

