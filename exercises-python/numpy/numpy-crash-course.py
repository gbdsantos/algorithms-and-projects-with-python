import numpy as np

mylist = [1, 2, 3, 4]

np.array(mylist)

mylist

type(mylist)

arr = np.array(mylist)

type(arr)

arr

a = np.arange(0,10)
a

a = np.arange(0, 10, 2)
a

np.zeros((5,5))

np.zeros((1,10))

np.ones((2,4))

np.random.randint(0,100)

np.random.randint(0,100,(5,5))

np.linspace(0, 10, 6)

np.linspace(0, 10, 101)

np.random.seed(101)

np.random.randint(0,100,10)

arr = np.random.randint(0,100,10)
arr.max()
arr.min()
arr.mean()
arr.argmax()
arr.argmin()

arr.reshape(2,5)

mat = np.arange(0,100).reshape(10,10)
mat
mat[5,2]

mat[:,2]
mat[2,:]

mat > 50

mat[mat>50]