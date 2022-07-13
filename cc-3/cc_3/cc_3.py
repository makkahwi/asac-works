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

        for char in str(key):
            ascii = ord(char)
            sum += ascii

        hkey = (sum * 19) % self.size

        return hkey


if __name__ == "__main__":
    pass


def fibonacci(n):
    if not isinstance(n, int) or n <= 0:
        raise Exception("Should have an input of a postive integer")

    x = 0

    ht = Hashtable()
    ht.set(0, 1)
    ht.set(1, 1)

    while x <= n:
        if x != 0 and x != 1:
            ht.set(x, ht.get(x - 1)[0][1] + ht.get(x - 2)[0][1])

        x += 1

    return ht.get(n - 1)[0][1]
