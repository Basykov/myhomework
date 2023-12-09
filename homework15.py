# Task 1

class Animal:
    def talk(self):
        print("Generic sound")

class Cat(Animal):
    def talk(self):
        print("Meow meow")

class Dog(Animal):
    def talk(self):
        print("Woof woof")


def animtalk(animal):
    animal.talk()

dog = Dog()
cat = Cat()

animtalk(dog)
animtalk(cat)

# Task2 

class Author:
    def __init__(self, name, country, birthday):
        self.name = name 
        self.country = country
        self.birthday = birthday
        self.books = []
    def __str__(self):
        return f"{self.name} is from {self.country} and was born at {self.birthday}"
    def __repr__(self):
        return f"Name: {self.name}, Country: {self.country}, Birthday: {self.birthday}"
        

class Book:
    allbooks = 0
    def __init__(self, name, year, author:Author):
        self.name = name 
        self.year = year
        self.author = author
        Book.allbooks += 1

    def __str__(self):
        return f"{self.name} is written by {self.author} and was created at {self.year}"
    def __repr__(self):
        return f"Name: {self.name}, Author: {self.author}, Year: {self.year}"


class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books = []
        self.authors = []
    def new_book(self, name: str, year: int, author: Author):
        b = Book(name, year, author)
        self.books.append(b) 
        return b
    def group_by_author(self, author: Author):
        c = []
        for i in self.books:
            if i.author == author:
                c.append(i)
        return c
    def group_by_year(self, year: int):
        g = []
        for i in self.books:
            if i.year == year:
                g.append(i)
        return g
    def __str__(self):
        return f"{self.name} has books: {self.books} and Authors {self.authors}"
    def __repr__(self):
        return f"Name: {self.name}, Authors: {self.authors}, books: {self.books}"

aut1 = Author("Jhon","America","October 25")
aut2 = Author("Bob","Canada", "December 13")

print(aut1.__str__())
print(aut2.__repr__())

libr = Library("Good Book")

b1 = libr.new_book("Joshuas journey", 2002, aut1)
b2 = libr.new_book("Joshuas journey2", 2005, aut1)
b3 = libr.new_book("Joshuas journey3", 2007, aut1)
b4 = libr.new_book("Joshuas journey4", 2012, aut1)
b5 = libr.new_book("1322", 2005, aut2)
b6 = libr.new_book("Nevermore", 2012, aut2)
print(b1.__str__())
print(b4.__repr__())
print(libr.books)

print("\n")

print(libr.group_by_author(aut1))

print("\n")

print(libr.group_by_year(2005))



# Task 3 Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *)
#  з належною перевіркою й обробкою помилок.
#  Потрібно додати магічні методи для математичних операцій та операції порівняння між об'єктами класу Fraction

print("\n")

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def simplify(self):
        common = self.gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def __add__(self, other):
        new_num = self.numerator * other.denominator +  other.numerator * self.denominator
        new_denum = self.denominator * other.denominator
        return Fraction(new_num, new_denum)
    
    def __sub__(self, other):
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_denom = self.denominator * other.denominator
        return Fraction(new_num, new_denom)
    
    def __mul__(self, other):
        new_num = self.numerator * other.numerator
        new_denum = self.denominator * other.denominator
        return Fraction(new_num, new_denum)
    
    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Division by zero is not allowed")
        new_num = self.numerator * other.denominator
        new_denum = self.denominator * other.numerator
        return Fraction(new_num, new_denum)
    
    def __eq__(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    c =  x + y 
    print(c)