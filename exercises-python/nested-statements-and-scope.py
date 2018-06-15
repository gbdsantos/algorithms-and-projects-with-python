#L: Local, onde 'Local' se refere que a variável está presente dentro da função
#Exemplo 1
lambda num : num**2

#Exemplo 2
#Global
name = 'THIS IS A GLOBAL STRING'

def greet():
    #Enclosing
    name = 'Sammy'

    def hello():
        #Local
        name = 'I AM LOCAL'
        print('Hello '+ name)
    hello()
greet()

#Exemplo 3
x = 50
def func(x):
    print(f'X is {x}')

    #LOCAL REASSIGMENT
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')


#Exemplo 4 - Atribuído valor de uma variável local para a variável global
x = 50
def func(x):
    global x
    print(f'X is {x}')

    #LOCAL REASSIGMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')

print(x)
func()
print(x)

#Exemplo 4 - Não usando a GLOBAL. Maneira mais segura e que facilita o DEBUG
x = 50
def func(x):
    global x
    print(f'X is {x}')

    #LOCAL REASSIGMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE'
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')
    return x

x = func(x)
print(x)