# task 1 Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys 
# and the number of occurrences as values. 

print("\n")

string_task1 = input("enter your string:\n")

strspl = string_task1.split()

task1_dict = {}

for i in strspl:
    if i in task1_dict.keys():
        task1_dict[i] += 1
    else:
        task1_dict[i] = 1
print(task1_dict)



# task 2 Compute the total price of the stock where the total price is the sum of the price of an item multiplied 
# by the quantity of this exact item.
# The code has to return the dictionary with the sums of the prices by the goods types.
print("\n")

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
diktallsum = {}

for i, b in stock.items():
    diktallsum[i] = b * prices[i]

print(diktallsum)



# task3 Use a list comprehension to make a list containing tuples
# (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.

list_task3 = [(i,i**2) for i in range(1,11)]

print(list_task3)



# task 4 
    # Створити лист із днями тижня.
    # В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
    # Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,
print("\n")

list_task4 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
dict_1_task4 = {i: x for i, x in zip(range(1,8), list_task4)}
dict_2_task4 = {i: x for i, x in zip(list_task4, range(1,8))}
print(dict_1_task4)
print(dict_2_task4)