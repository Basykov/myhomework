from django.test import TestCase
from mypolls.models import Person, Anything, Note

class Person_TestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name = "TT", last_name = "CC")
        Person.objects.create(first_name = "VV", last_name = "GG")

    def test_creation(self):
        Person_1 = Person.objects.get(first_name = "TT")
        Person_2 = Person.objects.get(first_name = "VV")
        self.assertEqual(Person_1.last_name ,"CC")
        self.assertEqual(Person_2.last_name , "GG")
        self.assertEqual(Person_1.first_name , "TT")
        self.assertEqual(Person_2.first_name , "VV")


class Anything_TestCase(TestCase):
    def setUp(self):
        Anything.objects.create(something = "Bag", everything = "Bol")
        Anything.objects.create(something = "Tuck", everything = "Toll")

    def test_creation(self):
        Anything_1 = Anything.objects.get(something = "Bag")
        Anything_2 = Anything.objects.get(something = "Tuck")
        self.assertEqual(Anything_1.everything ,"Bol")
        self.assertEqual(Anything_2.everything , "Toll")
        self.assertEqual(Anything_1.something , "Bag")
        self.assertEqual(Anything_2.something , "Tuck")

class Note_TestCase(TestCase):
    def setUp(self):
        Note.objects.create(title = "BBs", text = "GGf", reminders = "", category = "Work" )
        Note.objects.create(title = "Hhr", text = "Ttv", reminders = "", category = "Work")

    def test_creation(self):
        Note_1 = Anything.objects.get(title = "BBs")
        Note_2 = Anything.objects.get(title = "Hhr")
        self.assertEqual(Note_1.text ,"GGf")
        self.assertEqual(Note_2.text , "Ttv")
        self.assertEqual(Note_1.reminders , "")
        self.assertEqual(Note_2.category , "Work")

