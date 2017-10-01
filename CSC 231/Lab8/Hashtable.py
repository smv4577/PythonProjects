import math


class HashTable:
    def __init__(self):
        """
        Constructor sets the default number of slots to 11.
        """
        self.size = 11
        self.items = 0
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        """ Inserts data into the hash table using the key.
        :param key: An integer or string used as the hash value.
        :param data: The data to be inserted.
        :return: Nothing is returned.
        """

        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            self.items += 1

        # along with delete function
        elif self.data[hashvalue] == "None":
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
            self.items += 1

        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace

            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] is not None and \
                        self.slots[nextslot] is not key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                    self.items += 1
                else:
                    self.data[nextslot] = data  # replace

        if self.items / self.size > .5:
            oldSlots = self.slots.copy()
            oldData = self.data.copy()
            newSize = 2 * self.size + 1

            while not self.isPrime(newSize):
                newSize += 2
            self.slots = newSize * [None]
            self.data = newSize * [None]
            self.size = newSize
            self.items = 0

            for index in range(len(oldSlots)):  # O(N)
                if oldSlots[index] is not None:
                    self.put(oldSlots[index], oldData[index])

            # print(self.size)
            # print(self.items/self.size)

    def hashfunction(self, key, size):
        """
        Computes the index given a particular key.
        :param key: An integer or string used as the key.
        :param size: The size of the hash table.
        :return: The computed index.  This method may thrown an exception
        if the key is not an integer or a string.
        """
        if type(key) is int:
            return key % size
        elif type(key) is str:
            sum = 0
            for pos in range(len(key)):
                sum += ord(key[pos])

            return sum % size
        else:
            raise Exception("Invalid key in hash function: " + str(key))

    def rehash(self, oldhash, size):
        """
        Returns a new hash value.  Used in the event of a collision.  Linear probing
        is the resolution.
        :param oldhash: The old hash value.
        :param size: The size of the hash table.
        :return: The new hash value.
        """
        return (oldhash + 1) % size

    def get(self, key):
        """
        Retrieves the data from the hash table at a particular key.
        :param key: The key to use to retrieve the data.
        :return: The data at a particular key.
        """
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False

        # deleted = "None" # maybe ???? idk ????

        position = startslot
        while self.slots[position] is not None and \
                not found and not stop:  # and deleted: # maybe? idk
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        """ Overrides getitem so that a programmer can use the square bracket notation.
        :param key: The key in the hash table.
        :return: The value at that key.
        """
        return self.get(key)

    def __setitem__(self, key, data):
        """ Overrides setitem so that a programmer can use the square bracket notation.
        :param key: The key to use.
        :param data: The data to store at that key.
        :return: Nothing returned.
        """
        self.put(key, data)

    def __len__(self):  # O(1)
        return self.items

    def isPrime(self, key):  # O(N)
        if key < 2:
            return False
        elif key % 2 == 0 and key > 2:
            return False
        for i in range(3, int(math.sqrt(key))):
            if key % i == 0:
                return False
        return True

    def delete(self, key):  # fix
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = None
                self.slots[position] = "None"
                self.data[position] = None
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        self.items -= 1

# myTable = HashTable()
# myTable[1] = "dog"
# print("The length of the table is", len(myTable))
# print("The value at key 1 is ", myTable[1])
# myTable.delete(1)
# print("The length of the table is", len(myTable))
# print("The value at key 1 is ", myTable[1])
# myTable[1] = "dog"
# myTable[12] = "cat"
# myTable[23] = "elephant"
# print("The length of the table is", len(myTable))
# print("The value at key 1 is ", myTable[1])
# print("The value at key 12 is ", myTable[12])
# print("The value at key 23 is ", myTable[23])
# myTable.delete(1)
# myTable.delete(12)
# print("The length of the table is", len(myTable))
# print("The value at key 1 is ", myTable[1])
# print("The value at key 12 is ", myTable[12])
# print("The value at key 23 is ", myTable[23])
# myTable[1] = "parrot"
# print("The length of the table is", len(myTable))
# print("The value at key 1 is ", myTable[1])
# print("The value at key 12 is ", myTable[12])
# print("The value at key 23 is ", myTable[23])
