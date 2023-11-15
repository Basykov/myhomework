#task 1 Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except state­ment to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?
def Oops():
    raise IndexError
def opscatch():
    try:
        Oops()
    except IndexError:
        print("cought you")

opscatch()
def Oops():
    raise KeyError

# opscatch() видає помилку бо відловлює лише IndexError а ми змінили Oops на інший exeption



# task 2 Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).    


def task2fun(a,b):
    j = (a*a)/b
    return j
try:
    h = int(input("num1:  "))
    d = int(input("num2:  "))
    print(task2fun(h,d))
except ZeroDivisionError:
    print("Zero? are you serious?")
except ValueError:
    print("I said NUMBERS")