# Write a Python program to detect the number of local variables declared in a function.

def functask1():
    a = 3
    b ="asda"
    c = [1,2,4,6]
    d = False
    ltas1 = locals()
    return len(ltas1)
print(functask1())

# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def functask2():
    rest2 = functask1() + 1
    return rest2
print(functask2())


# Write a function called "choose_func" which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one


nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def firsfun3(*a):
    return sum([i**3 for i in a])

def secfun3(*a):
    j = 0
    for i in a:
        j += i
    return j
def choose_func(a,func1,func2):
    if all(i>0 for i in a):
        return func1(*a)
    else:
        return func2(*a)

print(choose_func(nums1, firsfun3, secfun3))
print(choose_func(nums2, firsfun3, secfun3))
