myString = 'hello'
mylist = [letter for letter in myString]
mylist

#Example 2
mylist = [x for x in 'word']
mylist

#Example 3
mylist = [num for num in range(0, 10)]
mylist

#Example 4
mylist = [num**2 for num in range(0, 10)]
mylist

#Example 5
mylist = [x for x in range(0, 11) if x % 2 == 0]
mylist

#Example 6
celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)* temp + 32) for temp in celcius]
fahrenheit

#Example 7
results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]

#Example 8
mylist = []

for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        mylist.append(x*y)

mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 1000]]
mylist