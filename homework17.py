# Task 1

# Create your own implementation of a built-in function enumerate, named 'with_index', which takes two parameters:
# 'iterable' and 'start', default is 0. 

print("\n")
print("Task 1")

c = ["a", "b", "c", "f"]
def with_index(iterable, start = 0):
    for i in range(start, len(iterable) + start):
        yield i, iterable[i-start]

for index, item in with_index(c):
    print(f'Index: {index}, Item: {item}')

# Task 2

# Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
# 'start', 'end', and optional step. 

print("\n")
print("Task 2")

def in_range(start, end, step = 1):
    while start <= end:
        yield start
        start += step

for num in in_range(1, 10, 2):
    print(num)

# Task 3 

# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.

print("\n")
print("Task 3")

class My_Iterable:
    def __init__(self, data):
        self.elements = data
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.elements):
            current_element = self.elements[self.index]
            self.index += 1
            return current_element
        else:
            raise StopIteration
    
    def __getitem__(self, index):
        return self.elements[index]
    
c = [1, 2, 3, 4, 5]
custom_iterable = My_Iterable(c)


print("Using for loop:")
for item in custom_iterable:
    print(item)

print("\nUsing square brackets syntax:")
print(custom_iterable[2])  
print(custom_iterable[4])  