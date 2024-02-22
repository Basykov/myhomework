my_working_stack = ['a','b','c','d','e',"f","g",]

def restructure_stuck(stuck:list):
    new_stuck = []
    for _ in range(len(stuck)):
        new_stuck.append(stuck.pop())
    return new_stuck

print(my_working_stack)

result = restructure_stuck(my_working_stack)

print(result)
print(my_working_stack)