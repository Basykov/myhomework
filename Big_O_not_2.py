class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(input_str):

    stack = Stack()

    for i in input_str:
        stack.push(i)

    reversed_str = ""

    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

if __name__ == "__main__":
    input_str = input("Enter a your prophesy: ")
    reversed_str = reverse_string(input_str)
    print("Reversed sequence:", reversed_str)