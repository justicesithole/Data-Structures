#Class iterator
#Iterates Items in a class

class iterator:

    def __init__(self, item_list):
        self.bag_list = item_list
        self.current_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_item < len(self.bag_list):
            item = self.bag_list[self.current_item]
            self.current_item += 1
            return item
        else:
            raise StopIteration

#This is a metaclass
#You take the class and use it inside another class in the iterator method
#Then you use it as follows
        #items = major_class()
        #for item in items:
            #print(item)
