import string


class Hashtable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def set(self, key, value):
        """
        This method hashes the key, and set the key and value pair in the table.

        Input:
        key, value

        Output:
        no output
        """
        hkey = self.hash(key)

        if self.table[hkey] == None:
            self.table[hkey] = [(key, value)]
        else:
            self.table[hkey].append((key, value))

    def get(self, key):
        """
        This method finds the value with associated key given

        Input:
        key

        Output:
        associated value
        """
        hkey = self.hash(key)

        return self.table[hkey]

    def contains(self, key):
        """
        This method indicates if the key exists in the table

        Input:
        key

        Output:
        boolean indicator
        """
        hkey = self.hash(key)

        if self.table[hkey] == None:
            return False
        else:
            return True

    def keys(self):
        """
        This method to list down keys of the table

        Input:
        None

        Output:
        array of keys
        """
        keys = []

        for value in self.table:
            if value:
                for pair in value:
                    keys.append(pair[0])

        return keys

    def hash(self, key):
        """
        This method hashes the key

        Input:
        key

        Output:
        hashed key
        """
        sum = 0

        for char in key:
            ascii = ord(char)
            sum += ascii

        hkey = sum % self.size

        return hkey


def repeated_word(text):
    """
    To find the first word to occur more than once in a string

    Input:
    given text

    Output:
    the first repeated word
    """

    # Turn text into a list of split words without punctuations
    text = text.translate(str.maketrans("", "", string.punctuation)).lower().split()

    ht = Hashtable()

    for word in text:
        if ht.get(word):
            return word
        else:
            ht.set(word, 1)

    for word in text:
        ht.set(word, 1)

    return "No Repeated Words"


if __name__ == "__main__":
    pass
