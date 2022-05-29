class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Pre-order type
    def pre_order(self):

        if not self.root:
            return "The tree is empty"

        current = self.root

        result = []

        def _walk(current):
            result.append(current.value)

            if current.left:
                _walk(current.left)

            if current.right:
                _walk(current.right)

        _walk(current)

        return result


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

        for char in str(key):
            ascii = ord(char)
            sum += ascii

        hkey = (sum * 19) % self.size

        return hkey


def tree_intersection(t1, t2):
    """
    A function to extract the common values of two binary trees.

    Input:
    two trees

    Output:
    arr of common values
    """

    ht = Hashtable()

    arr1 = t1.pre_order()
    arr2 = t2.pre_order()
    common = []

    for node in arr1:
        ht.set(node, 1)

    for node in arr2:
        if ht.contains(node):
            common.append(node)

    return common


if __name__ == "__main__":
    pass
