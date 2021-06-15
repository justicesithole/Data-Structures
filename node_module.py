#A node that can be used in a linked list

class node:

    def __init__(self, a, b = None, c = None):
        self.data = a
        self.next = b
        self.prev = c

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev

