class UnsortedList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        return self.items.index(item)

    def pop(self, index=None):
        if index is None:
            return self.items.pop()
        else:
            return self.items.pop(index)

    def insert(self, index, item):
        self.items.insert(index, item)

    def slice(self, start, stop):
        return self.items[start:stop]


if __name__ == "__main__":
    my_list = UnsortedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)

    print("Origin:", my_list.items)

    my_list.append(6)
    print("After:", my_list.items)

    print("Index 3:", my_list.index(3))

    popped_item = my_list.pop()
    print("Popped item:", popped_item)
    print("After pop():", my_list.items)

    my_list.insert(2, 7)
    print("After insert(2, 7):", my_list.items)

    sliced_list = my_list.slice(1, 4)
    print("Sliced:", sliced_list)