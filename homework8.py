# task 1 Make a directory with 2 modules; make a function in one of them;
# then import this function in the other module and use that in your script of choice.

# second module is homework8.1.py

import homework8imp

print("\n")
homework8imp.task1_func()

# task 2 The “sys.path” list is initialized from the PYTHONPATH environment variable.
#  Is it possible to change it from within Python?
#  If so, does it affect where Python looks for module files? Run some interactive tests to find it out.
# Я не завантажував папку importtraining щоб не засоряти гітхаб, але воно працює і по ідеї працюватиме з іншими папками модулів.

import sys

print(sys.path)

new_direct = "C:/Programming/Homework/importtrainning"
sys.path.append(new_direct)
print("\n")

print(sys.path)

try:
    import lineworkimp 
    print("good")
except ImportError:
    print("eror")


# task 3 теж використовує homework8imp щоб не створювати зайвих файлів.

print(homework8imp.task3test("C:/Programming/txt files/Probe.txt"))
print(homework8imp.task3test("C:\Programming\Homework\homework8imp.py"))
