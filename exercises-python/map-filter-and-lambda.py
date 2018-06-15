#Map
def square(num):
    return num**2

my_nums = [1, 2, 3, 4, 5]

#Usando for
for item in map(square, my_nums)
    print(item)

#Transformando os resultados em uma lista
list(map(square, my_nums))

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']
list(map(splicer, names))

#Filter
def check_even(num):
    return num % 2 == 0

mynums = [1, 2, 3, 4, 5, 6]

filter(check_even, mynums)

list(filter(check_even, mynums))

for n in filter(check_even, mynums)
    print(n)

#Lambda
#Função Original:
def square(num):
    result = num ** 2
    return result

#Refatorando:
def square(num):
    return num ** 2

#Refatorando I:
def square(num):  return num ** 2

#Refatorando II:
lambda num : return num ** 2

#Refatorando III e resultado no formato de expressão lambda
lambda num: num ** 2
square = lambda num: num ** 2

square(5)

#Usando em conjunto com Map e Filter
list(map(lambda num: num ** 2, mynums))
list(filter(lambda num: num % 2 == 0, mynums))

list(map(lambda name: name[0], names))
list(map(lambda name: name[::-1], names))