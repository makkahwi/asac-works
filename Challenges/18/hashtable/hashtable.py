class Hashtable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def set(self, key, value):
        hkey = self.hash(key)

        if self.table[hkey] == None:
            self.table[hkey] = [(key, value)]
        else:
            self.table[hkey].append((key, value))

    def get(self, key):
        hkey = self.hash(key)

        return self.table[hkey]

    def contains(self, key):
        hkey = self.hash(key)

        if self.table[hkey] == None:
            return False
        else:
            return True

    def keys(self):
        keys = []

        for value in self.table:
            if value:
                for pair in value:
                    keys.append(pair[0])

        return keys

    def hash(self, key):
        sum = 0

        for char in key:
            ascii = ord(char)
            sum += ascii

        hkey = sum % self.size

        return hkey


if __name__ == "__main__":
    pass
