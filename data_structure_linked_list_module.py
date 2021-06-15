#Implementing Abstract Data Type using a linked list

from unordered_linked_list_module import unordered_list

#Stack ADT
class stack:
    def __init__(self):
        self.items = unordered_list()

    def is_empty(self):
        return self.items.is_empty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        return self.items.pop_pos(0)

    def peek(self):
        return self.items.pos(0)

    def size(self):
        return self.items.size()

    def show(self):
        return self.items.show()

#Queue ADT
class queue:

    def __init__(self):
        self.items = unordered_list()

    def is_empty(self):
        return self.items.is_empty()

    def enqueue(self, item):
        self.items.add(item)
        
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return self.items.size()

    def show(self):
        return self.items.show()




