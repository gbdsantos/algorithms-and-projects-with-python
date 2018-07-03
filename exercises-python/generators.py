def create_cubes(n):

    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)

create_cubes(10)
list(create_cubes(10))

#WITHOUT GENERATOR
def gen_fibon(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a, b = b, a + b
    return output


#WITH GENERATOR
def gen_fibon(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b

for number in gen_fibon(10):
    print(number)

#Exemple
def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()
g

print(next(g))

#TypeError
s = 'hello'

for letter in s:
    print(letter)

next(s)

#Resolve to Error
s_iter = iter(s)
next(s_iter)

