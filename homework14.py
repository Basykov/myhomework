# Task 1

print("\n")

class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def getinf(self):
        return f"Name: {self.name} {self.surname}, Age: {self.age}"
class Teacher(Person):
    def __init__(self, name, surname, age, salary, lessoncount):
        super().__init__(name, surname, age)
        self.salary = salary
        self.lessoncount = lessoncount
    def premium(self):
        b = self.lessoncount * 300
        return b
class Student(Person):
    def __init__(self, name, surname, age, classnum):
        super().__init__(name, surname, age)
        self.classnum = classnum
    def newyear(self):
        self.classnum += 1
        return self.classnum
    
person1 = Person("Alice","Barrow", 30)
print(person1.getinf())

teacher1 = Teacher("Jhon","Smith", 45, 50000, 17)
print(teacher1.getinf()) 
print(teacher1.premium())  
print(teacher1.salary)
print(teacher1.lessoncount)


student1 = Student("Bob","Weaver", 20, 3)
print(student1.getinf())  
print(student1.newyear())  
print(student1.classnum)




# Task 2 

class Mathematician:
    @staticmethod
    def square_nums(nums):
        return [num ** 2 for num in nums]

    @staticmethod
    def remove_positives(nums):
        return [num for num in nums if num <= 0]
    
    @staticmethod
    def filter_leaps(date):
        b = []
        for i in date:
            if i % 4 == 0:        
                b.append(i)
        return b
    
m = Mathematician()

g = [1,2,3,4,5]
d = [2000, 2002, 2004, 2008, 2013, 2020]
c = [-1,2,-3,4,5]

print(m.filter_leaps(d))
print(m.remove_positives(g))
print(m.square_nums(g))
print(m.remove_positives(c))






# Task 3



class Product:

    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:

    def __init__(self):
        self.products = []
        self.income = 0

    def add(self,product,amount):
            for i in self.products:
                if product.name == i["name"]:
                    i["quantity"] += amount
                    return self.products
                
            self.products.append({
                "type": product.type,
                "name": product.name,
                "price": product.price * 1.30,
                "quantity": amount,
                "discount": 0
            })
            return self.products
    
    def set_disc(self, id, disc):
        for i in self.products:
            if id == i["name"] or id == i["type"]:
                i["discount"] = disc
                return self.products
            else:
                raise ValueError (f"{id} is incorrect")
            
    def sell_prod(self, name, amount):
        for i in self.products:
            if name == i["name"]:
                if i["discount"] !=0:
                    b = i["price"] * (i["discount"]/100) * amount
                else:
                    b = i["price"] * amount
                self.income += b
                i["quantity"] -= amount
                return self.products, self.income
    def get_inc(self):
        print(self.income)
    def get_all_prod(self):
        print(self.products)
    def get_product_info(self, name:str):
        for i in self.products:
            if name == i["name"]:
                return(i["name"],i["quantity"])
        



p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 20)
print(s.products)
s.add(p, 30)
s.set_disc("Football T-Shirt", 30)
print(s.products)
s.add(p2, 300)
print(s.products)
s.sell_prod('Ramen', 10)
s.get_inc()
s.get_all_prod()
print(s.get_product_info("Football T-Shirt"))



# Task 4

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open('logs.txt', 'a+') as file:
            file.write(f'Error: {self.msg}\n')



raise CustomException("Woops?")

