import random

#task1
print("\n")
list_task1 = []
while len(list_task1) < 10:
    list_task1.append(random.randint(1,100))
print(max(list_task1))

#task2
print("\n")
list1_task2 = []
list2_task2 = []
cummon_numbers_list = []
while len(list1_task2) < 10:
    list1_task2.append(random.randint(1,10))
    list2_task2.append(random.randint(1,10))
print(list1_task2)
print(list2_task2)
for i in list1_task2:
    if i not in cummon_numbers_list:
        if i in list2_task2:
            cummon_numbers_list.append(i)
print(cummon_numbers_list)

#task3
print("\n")

numbers_list_task3 = list(range(1,101))
index_in_list = 0
numbers_thatweneed_list_task3 = []
while index_in_list < len(numbers_list_task3):
    if numbers_list_task3[index_in_list] % 3 == 0 and numbers_list_task3[index_in_list] % 5 !=0:
        numbers_thatweneed_list_task3.append(numbers_list_task3[index_in_list])
    index_in_list +=1
print(numbers_thatweneed_list_task3)