mylist = [1, 2, 3]
mylist.append(4)
mylist.pop()
mylist

help(mylist.insert)

def name_function():
    '''
    DOCSTRING: Information about the function
    INPUT: no input...
    OUTPUT: Hello ..
    '''
    print('Hello')

name_function()

def say_hello(name='NAME'):
    return 'hello '+name

say_hello('Guilherme')

result = say_hello('Guilherme')


def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False

def dog_check(mystring):
    return 'dog' in mystring.lower()

def pig_latin(word):
    first_letter = word[0]

    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

pig_latin('word')
pig_latin('apple')
