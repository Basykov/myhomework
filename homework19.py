import logging
import unittest


# Task 1

class Open_file:
    def __init__(self, name: str, mode):
        self.name = name
        self.mode = mode
        self.counter = 0

    def __enter__(self):
        logging.info(f"Entering the context for file: {self.name}")
        self.file = open(self.name, self.mode)
        self.counter += 1
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.counter -= 1
        if exc_type is not None:
            logging.error(f"Exception occurred: {exc_type}, {exc_val}")
        logging.info(f"Exiting the context for file: {self.name}")
        self.file.close()

    def get_counter(self):
        return self.counter

# Task 2
class TestOpenFile(unittest.TestCase):
    def setUp(self):
        self.file_path = 'homework19.txt'

    def test_file_creation_and_counter(self):
        logging.basicConfig(level=logging.INFO)
        open_file_instance = Open_file(self.file_path, 'w')
        with open_file_instance as f:
            f.write('testing')
        self.assertEqual(open_file_instance.get_counter(), 0) 
    
    
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            open_file_instance = Open_file('non_existing_file.txt', 'r')
            with open_file_instance as f:
                pass  
            
    
    def test_file_open_for_reading(self):
        with open(self.file_path, 'w') as test_file:
            test_file.write('test content')
        open_file_instance = Open_file(self.file_path, 'r')
        with open_file_instance as f:
            self.assertEqual(f.read(), 'test content')  

    def tearDown(self):
        logging.disable() # Щоб логг виводився лише при сетапі.


if __name__ == '__main__':
    unittest.main()

# Task 3 опціональний тому я його не робив =0.