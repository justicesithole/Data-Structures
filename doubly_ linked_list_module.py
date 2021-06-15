from node_module import node

#A List Abstract Data Type

class doubly_list:

    def __init__(self):
        self.head = None
        self.count_size = 0

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = node(item, self.head)
        if self.head:
            self.head.set_prev(temp)
        self.head = temp
        

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        self.count_size = count

        return count
    
    def pop_pos(self, num):
        data = ""
        current = self.head
        previous = None
        pos = 0
        self.index = num 
        found = False
        while pos <= self.index:
            data = data + str(current.get_data())
            if pos == self.index:
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
            previous = current
            current = current.get_next()
            
            pos = pos + 1
        return data

    def pop(self):
        data = ""
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        current = self.head
        previous = None
        pos = 0
        self.index = count - 1
        found = False
        while pos <= self.index:
            data = str(current.get_data())
            if pos == self.index:
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                    
            previous = current
            current = current.get_next()
            
            pos = pos + 1
        return data

    def pos(self, num):
        pos = num
        item = ""
        data = ""
        current = self.head
        item = item + str(current.get_data())
        while current != None:
            data = str(current.get_data())
            current = current.get_next()
        if pos == 0:
            return item
        else:
            return data
    

    def indexs(self,item):
        count = 0
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                count = count + 1

        if current == None:
            return "No such item exists in the list"
        else:
            return count
        

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def show(self):
        rep = "["
        data = ""
        count = -1
        current = self.head
        while current != None:
            rep = rep + str(current.get_data()) + ", "
            current = current.get_next()
        rep = rep[:-2] + "]"
        return rep
    

    def append(self, item):
        temp = node(item)
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        current = self.head
        previous = None
        pos = 0
        self.index = count - 1
        found = False
        rep = ""
        while pos < self.index:
            current = current.get_next()
            pos = pos + 1
        current.set_next(temp)
        rep = rep + str(current.get_data())
        return rep

    def inserts(self, pos, item):
        temp = node(item)
        current = self.head
        data = None
        count = 0 + 1
        if pos == 0:
            temp.set_next(self.head)
            self.head = temp
        while count < pos:
            current = current.get_next()
            count = count + 1
        
        #else:
        data = current.get_next()
        temp.set_next(data)
        current.set_next(temp)
            

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())



