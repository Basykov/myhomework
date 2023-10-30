#task1
print("\n")
sample_string = "hello world"
if len(sample_string) < 2 :
    print(sample_string)
else :
    print(sample_string[0:2] + sample_string[-2:])

#task2
print("\n")
phone_number = input("write your number" )
hasdigit = False
hasalpha = False
for i in phone_number :
    if i.isdigit() :
        hasdigit = True
    if i.isalpha() :
        hasalpha = True
if len(phone_number) == 10 and hasdigit == True and hasalpha == False:
    print("good number")
elif len(phone_number) > 10 :
    print("too long")
elif len(phone_number) < 10 :
    print("too short")
elif hasalpha == True :
    print("use only numbers")
else :
    print("eror")

#task3
print("\n")
user_answer = str(input("whats 7+3 "))
if int(user_answer) == 10:
    print ("True")
else :
    print("False")

#task4
print("\n")
my_name_task4 = "danylo"
my_name_task4_input = input("whrite your name ")
if my_name_task4_input.lower() == my_name_task4 :
    print("True")
else :
    print("False")