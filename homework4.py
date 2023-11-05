import random
#task1
print("\n")

computer_number = str(random.randint(1,10))
player_input_task1 = input("What number I have?\n")
while player_input_task1 != computer_number:
    player_input_task1 = input("try again\n")
print("you`re right")

#task2
print("\n")

name_task2 = input("what`s your name?\n")
age_task2 = int(input("how old are you?\n"))
print(f"Hello {name_task2}, on your next birthday you’ll be {age_task2+1} years")

#task3
print("\n")

user_input = input("Give me a word: ")
list_task3 = []
user_result = str()
for i in user_input:
    list_task3.append(i)
random.shuffle(list_task3)
for i in list_task3:
    user_result += i
print(user_result)
    