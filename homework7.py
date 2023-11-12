# task 1 Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print "My favorite movie is named {name}".
print("\n")

def favorite_movie(a):
    return (f"My favorite movie is {a}")

fav_mov = input("what`s your favorite movie?\n")
print(favorite_movie(fav_mov))



# task 2 Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. 
# Make the function print out the values of the dictionary to make sure that it works as intended.
print("\n")

def make_country(a,b):
    dikt_task2 = {a:b}
    print(dikt_task2)

make_country("Poland", "Warsaw")





# task 3 Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter 
# (to keep things simple let it only be '+', '-' or '*') and an arbitrary number of arguments (only numbers) as the second parameter. 
# Then return the sum or product of all the numbers in the arbitrary parameter. For example:

#     the call make_operation('+', 7, 7, 2) should return 16
#     the call make_operation('-', 5, 5, -10, -20) should return 30  >>>!!!! Я не розумію чому не 20? по ідеї мається на увазі -5 -5 --(або +)10 --(або +)20? але це буде 20 а не 30 в результаті.
#     the call make_operation('*', 7, 6) should return 42  
print("\n")

def make_op(a,*b):
    result_task4 = 0
    if a == "+":
        for i in b: 
            result_task4 += i
    if a == "-":
        for i in b: 
            result_task4 -= i
    if a == "*":
        result_task4 = 1
        for i in b: 
            result_task4 *= i
    return result_task4

print(make_op("+", 7, 7, 2))
print(make_op("-", 5, 5, -10, -20))
print(make_op("*", 7, 6))