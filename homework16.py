from functools import wraps  #for task 3

# Task 1

# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
#  passed to the constructor. The logic inside the `validate` method could be to check
#  if the passed email parameter is a valid email string.

print("\n")

class Mailcheck:
    def __init__(self, mail:str):
        self.mail = mail
        self.validate()

    def validate(self):
        if "@" not in self.mail:
            raise ValueError("Incorrect mail")
        if self.mail[self.mail.index("@") -1] == ".":
            raise ValueError("Incorrect mail")
        if self.mail[self.mail.index("@") -1] == "-":
            raise ValueError("Incorrect mail")
        if "#" in self.mail:
            raise ValueError("Incorrect mail")

        
# t = Mailcheck("abc.@mail.com")
# b = Mailcheck("abc-@mail.com")
# g = Mailcheck("a#bc@mail.com")
e = Mailcheck("abc@mail.com")
print(e.mail)

# Task 2

# Implement 2 classes, the first one is the Boss and the second one is the Worker.

# Worker has a property 'boss', and its value must be an instance of Boss.

# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!

print("\n")

class Boss:

    def __init__(self, id_: int, name: str, company: str):

        self.id = id_

        self.name = name

        self.company = company

        self.workers = []
 
    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)
        else:
            raise ValueError("Worker not found")
        
    def __str__(self):
        return f"{self.name} is boss"

 

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):

        self.id = id_

        self.name = name

        self.company = company

        self._boss = boss

    @property
    def Worker_Boss(self):
        return self._boss
    
    @Worker_Boss.setter
    def New_boss(self, newboss:Boss):
        self._boss = newboss
        return self._boss
    
    def __str__(self):
        return f"{self.id}, {self.name}"

boss1 = Boss(1, "John", "ABC Company")
boss2 = Boss(3, "Bob", "ABC Company")

worker1 = Worker(101, "Alice", "ABC Company", boss1)
worker2 = Worker(102, "Bob", "ABC Company", boss1)
worker3 = Worker(103, "Charlie", "ABC Company", boss1)

boss1.add_worker(worker1)
boss1.add_worker(worker2)
boss1.add_worker(worker3)

for i in boss1.workers:
    print (i)

print(worker1.Worker_Boss)
worker1.New_boss = boss2
print(worker1.Worker_Boss)



# Task 3
# Write a class TypeDecorators which has several methods for converting results
# of functions to a specified type (if it's possible):

# methods:

# to_int

# to_str

# to_bool

# to_float

print("\n")

class TypeDecorators:
    def __init__(self, function_):
        self.function_ = function_

    @property
    def to_str(self):
        @wraps(self.function_)
        def wrapper():
            return str(self.function_())
        return wrapper
    
    @property
    def to_int(self):
        @wraps(self.function_)
        def wrapper():
            try:
                return int(self.function_())
            except (TypeError, ValueError):
                return "incorrect data"
        return wrapper
    
    @property
    def to_bool(self):
        @wraps(self.function_)
        def wrapper():
            try:
                return bool(self.function_())
            except (TypeError, ValueError):
                return "incorrect data"
        return wrapper
    
    @property
    def to_float(self):
        @wraps(self.function_)
        def wrapper():
            try:
                return float(self.function_())
            except (TypeError, ValueError):
                return "incorrect data"
        return wrapper

def func_tsk3():
    b = [1,3,5]
    return b

def func_tsk3_2():
    c = 3
    return c

b = TypeDecorators(func_tsk3)
print(b.to_str())
print(b.to_int())
print(b.to_bool())
print(b.to_float())
print("\n")

c = TypeDecorators(func_tsk3_2)
print(c.to_str())
print(c.to_int())
print(c.to_bool())
print(c.to_float())
print("\n")