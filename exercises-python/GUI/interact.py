from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def func(x):
    return x

interact(func, x=10)

@interact(x=True, y=1.0)
def g(x,y):
    return (x,y)



