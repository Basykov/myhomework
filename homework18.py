import unittest
import json # Для 2го завдання
from unittest.mock import patch
from io import StringIO

from homework13 import TVController # Я імпортував і замінив щоб функціонал homework13 виконувався лише в __name__ == '__main__'


# Task 1
#  Pick your solution to one of the exercises in this module.
#  Design tests for this solution and write tests using unittest library. 

class Task_1_tester(unittest.TestCase):
    def setUp(self):
        CHANNELS = ["BBC", "Discovery", "TV1000"]
        self.controller = TVController(CHANNELS)

    def test_channels(self):
        self.assertEqual(self.controller.channels, ['BBC', 'Discovery', 'TV1000'])
        self.assertEqual(self.controller.current_channel(), 'You are watching BBC')

        self.controller.last_channel()
        self.assertEqual(self.controller.current_channel(), 'You are watching TV1000')

        self.controller.turn_channel(2)
        self.assertEqual(self.controller.current_channel(), 'You are watching Discovery')

        self.controller.next_channel()
        self.assertEqual(self.controller.current_channel(), 'You are watching TV1000')

        self.controller.previous_channel()
        self.controller.previous_channel()
        self.assertEqual(self.controller.current_channel(), 'You are watching BBC')

        self.assertEqual(self.controller.exists("BBC"), 'Yes')
        self.assertEqual(self.controller.exists(1), 'Yes')
        self.assertEqual(self.controller.exists("sdaaw"), 'no')
        self.assertEqual(self.controller.exists(4), 'no')



# Task 2

# Write tests for the Phonebook application, which you have implemented in module 1.
#  Design tests for this solution and write tests using unittest library
    
# Не імпортував, бо все одно довелося переробити щоб все було у функціях.

def add_info(b, c):
    jjst = input("What state?\n")
    jjn = input("Name?\n")
    jjs = input("Surname?\n")
    jjp = input("Phone?\n")
    
    if jjst in c:
        jjj = [jjn, jjs, jjp]
        jb = c[jjst]
        jb.append(jjj)
        c[jjst] = jb
    else:
        jjjj = [[jjn, jjs, jjp]]
        c[jjst] = jjjj
    
    with open(b, "w") as ttf:
        json.dump(c, ttf, indent=4)

def find_info():
    ff = input("Who?(enter person info or state)\n")
    
    with open("homework18t2.json", "r") as ggf:
        gg = json.load(ggf)
        if ff in gg.keys():
            print(gg[ff])
        else:
            for i in gg.values():
                for d in i:
                    hf = d[0] + " " + d[1]
                    if ff == hf or ff in str(d):
                        print(d)

def change_info():
    jj = input("(A)dd, (C)hange or (D)elete?\n")

    jja = {}
    with open("homework18t2.json", "r") as ddf:
        dd = json.load(ddf)
        for i in dd:
            jja[i] = dd[i]

    if jj.upper() == "A":
        add_info("homework18t2.json", jja)
    
    if jj.upper() == "D":
        jjd = input("Who do you wish to delete? Enter Name and surname(Example: Rosa Park)\n")
        for i in jja.values():
            for b in i:
                hh = b[0] + " " + b[1]
                if jjd == hh:
                    i.remove(b)
                    print("Phone deleted.")
        with open("homework18t2.json", "w") as ttf:
            json.dump(jja, ttf, indent=4)
    
    if jj.upper() == "C":
        found = False
        jjv = input("Who do you wish to change? Enter Name and surname(Example: Rosa Park) remember that old info will be deleted\n")
        for i in jja.values():
            for b in i:
                hh = b[0] + " " + b[1]
                if jjv == hh:
                    i.remove(b)
                    print("Old info deleted. Now enter new one")
                    add_info("homework18t2.json", jja)
                    found = True
                    break
            if found == True:
                break

class TestAddInfo(unittest.TestCase):
    @patch('builtins.input', side_effect=["California", "John", "Doe", "123456789"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_new_information(self, mock_stdout, mock_input):
        # Prepares an initial state
        initial_state = {}
        with open("homework18t2.json", "w") as f:
            json.dump(initial_state, f)

        # Calls the function
        add_info("homework18t2.json", initial_state)

        # Loads the saved state and checks for expected output
        with open("homework18t2.json") as f:
            updated_state = json.load(f)
            self.assertEqual(updated_state, {"California": [["John", "Doe", "123456789"]]})
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('builtins.input', side_effect=["A","California", "Bob", "Ross", "123456739"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_Change_Add(self, mock_stdout, mock_input):
        initial_state = {}
        with open("homework18t2.json", "w") as f:
            json.dump(initial_state, f)

        change_info()

        with open("homework18t2.json") as f:
            updated_state = json.load(f)
            self.assertEqual(updated_state, {"California": [["Bob", "Ross", "123456739"]]})
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('builtins.input', side_effect=["C","Bob Ross","New jercy", "Tom", "Sett", "123452739"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_Change_change(self, mock_stdout, mock_input):
        initial_state = {"California": [["Bob", "Ross", "123456739"]]}
        with open("homework18t2.json", "w") as f:
            json.dump(initial_state, f)

        change_info()

        with open("homework18t2.json") as f:
            updated_state = json.load(f)
            self.assertEqual(updated_state, {"California": [],"New jercy": [["Tom", "Sett", "123452739"]]})
    
    @patch('builtins.input', side_effect=["D","Bob Ross"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_Change_delete(self, mock_stdout, mock_input):
        initial_state = {"California": [["Bob", "Ross", "123456739"]]}
        with open("homework18t2.json", "w") as f:
            json.dump(initial_state, f)

        change_info()

        with open("homework18t2.json") as f:
            updated_state = json.load(f)
            self.assertEqual(updated_state, {"California": []})
    
    @patch('builtins.input', side_effect=["Bob", "Bob Ross", "Ross"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_Change_find(self, mock_stdout, mock_input):
        initial_state = {"California": [["Bob", "Ross", "123456739"]]}
        with open("homework18t2.json", "w") as f:
            json.dump(initial_state, f)

        find_info()
        self.assertEqual(mock_stdout.getvalue().strip(), "['Bob', 'Ross', '123456739']")

        find_info()
        self.assertEqual(mock_stdout.getvalue().strip(), "['Bob', 'Ross', '123456739']\n['Bob', 'Ross', '123456739']")

        find_info()
        self.assertEqual(mock_stdout.getvalue().strip(), "['Bob', 'Ross', '123456739']\n['Bob', 'Ross', '123456739']\n['Bob', 'Ross', '123456739']")
        




if __name__ == "__main__":
    unittest.main()