#Hash Map Module


#Hash Map for pairs

class hash_map_pair:

    def __init__(self, size = None):
        self.size = size
        self.map = [None] * self.size

    def __get__hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    
    def add(self, key, value = None):
        key_hash = self.__get__hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.__get__hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.__get__hash(key)

        if self.map[key_hash] is None:
            return False

        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print("---PHONEBOOK----")
        for item in self.map:
            if item is not None:
                print(str(item))

#Hash Maps for integers

class hash_map_int:
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def __get__hash(self, key):
        hash = key
        return hash % self.size
    
    def add(self, key):
        key_hash = self.__get__hash(key)
        key_value = [key]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.__get__hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[0]
        return None

    def delete(self, key):
        key_hash = self.__get__hash(key)

        if self.map[key_hash] is None:
            return False

        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print("---PHONEBOOK----")
        for item in self.map:
            if item is not None:
                print(str(item))

#Hash Map for single items

class hash_map_single:
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def __get__hash(self, key):
        hash = 0
        count = 1
        for char in str(key):
            hash += (ord(char) * count)
            count += 1
        return hash % self.size
    
    def add(self, key):
        key_hash = self.__get__hash(key)
        key_value = [key]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.__get__hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[0]
        return None

    def delete(self, key):
        key_hash = self.__get__hash(key)

        if self.map[key_hash] is None:
            return False

        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print("---PHONEBOOK----")
        for item in self.map:
            if item is not None:
                print(str(item))
