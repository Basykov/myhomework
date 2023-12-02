from functools import wraps
import time

# Спробуйте модифікувати попередній приклад, додавши якийсь свій функціонал

print("\n")

def uppercase_decorator(func):
    @wraps(func)
    def wrapper():
        f = func().capitalize()
        c = func().upper()
        b = func().replace("l", "r")
        return f"{f} \n{c} \n{b}"
    return wrapper


@uppercase_decorator
def say_hi():
    "This will say hi"
    return 'hello there'

print(say_hi())

# 2. Напишіть декоратор, який виводить час виконання функції.

print("\n")

def timecheck(func):
    @wraps(func)
    def wrapper(*args):
        c = time.perf_counter()
        func(*args)
        b = time.perf_counter()
        f = b - c
        return f
    return wrapper

@timecheck
def myfunc(n):
    c = []
    j = []
    for i in range(1,n+1):
        c.append(i)
    for i in c:
        j.append(i * i)
    return j

print(myfunc(1000))






# 3. Створіть декоратор, який перевіряє аргументи, передані у функцію,
# і виводить повідомлення про помилку, якщо аргументи не задовольняють певні умови.

print("\n")

def lokk(func):
    @wraps(func)
    def wrapper(x):
        if x != 3:
            return "where is my 3?"
        else:
            return func(x)
    return wrapper
        
@lokk
def ff(a):
    b = a*a
    return b

print(ff(4))
print(ff(3))
