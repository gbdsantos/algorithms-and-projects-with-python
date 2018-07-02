
def add(n1, n2):
    print(n1 + n2)

add(10, 20)

number1 = 10
number2 = input("Please provide a number:")

add(number1, number2)
print("Something happened")

try:
    result = 10 + '10'

except:
    print("Hey it look like you aren't adding correctly!")
else:
    print("Add went well!")
    print(result)

try:
    f = open('testfile', 'w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("He you have an OS error")
finally:
    print("I always run")

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number:"))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")