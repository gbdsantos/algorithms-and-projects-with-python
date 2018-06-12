def myfunc(a, b, c=0, d=0, e=0):
    # Returns 5% of the sum of a and b
    return sum((a, b, c, d, e)) *0.05

myfunc(40, 50)

#Recebe um tupla de parametros e são quantos você desejar
def myfunc(*args):
    return sum(args) * 0.05
    print(args)

myfunc(40, 60, 100, 1, 34)


#Recebe um dicionário de parametros e são quantos você desejar
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit='apple', veggie='lettuce')

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))

myfunc(10, 20, 30, fruit='orange', food='eggs', animal='dog')

