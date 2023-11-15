# Used in homework 8 task 1 and 3

def task1_func():
    print("hello task 1")

def task3lines(a):
    filetas3 = open(a, "r")
    b = filetas3.readlines()
    filetas3.close()
    return len(b)
def task3char(a):
    filetas3t2 = open(a, "r")
    b = filetas3t2.read()
    filetas3t2.close()
    return len(b)
def task3test(a):
    c = task3char(a)
    b = task3lines(a)
    return c,b

