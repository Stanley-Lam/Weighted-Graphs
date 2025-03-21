import array_list as lst


class Dictionary:
    """
    A collection of key-value pairs
    NOTE: Do not alter this class.
    """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 5
        # The backing array:
        self.array = [None] * self.capacity
        # The number of pairs in this dictionary:
        self.size = 0

    def __eq__(self, other):
        if type(other) != Dictionary or self.size != other.size:
            return False

        keylist = keys(self)
        for i in range(lst.size(keylist)):
            key = lst.get(keylist, i)
            if get(self, key) != get(other, key):
                return False

        return True

    def __repr__(self):
        return "Dictionary(%d, %r, %d)"\
               % (self.capacity, self.array, self.size)


class Node:
    """
    A single node in a linked list
    NOTE: Do not alter this class.
    """

    def __init__(self, key, value, next):
        # The key contained in this node:
        self.key = key
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next

    def __eq__(self, other):
        return (type(other) == Node
                and self.key == other.key
                and self.value == other.value
                and self.next == other.next)

    def __repr__(self):
        return "Node(%r, %r, %r)" % (self.key, self.value, self.next)


def size(dct):
    """
    Calculate the size of a dictionary.
    TODO: Implement this function. It must have O(1) complexity.

    :param dct: A Dictionary
    :return: The size of the dictionary
    """
    return dct.size


def get(dct, key, default = None):
    """
    Get the value to which a key is mapped.
    TODO: Implement this function. It must have O(1) complexity.

    :param dct: A Dictionary
    :param key: A hashable key whose value to get
    :param default: A default value
    :return: The value to which the key maps, the default if it does not exist
    """
    new_key = hash(key) % dct.capacity

    current_node = dct.array[new_key]

    while current_node is not None and current_node.key != key:
        current_node = current_node.next
    if current_node is None:
        return default

    return current_node.value


def insert(dct, key, value):
    """
    Insert a key, overwriting any existing value, rehashing first if necessary.
    TODO: Implement this function. It must have O(1) complexity.

    :param dct: A Dictionary
    :param key: A hashable key to be inserted
    :param value: A value to which to map the key
    """
    old_capacity = dct.capacity
    if dct.size == dct.capacity:
        dct.capacity = dct.capacity * 2 + 1
        old_array = dct.array
        new_array = [None] * dct.capacity
        dct.array = new_array

        for i in range(0, old_capacity):
            current_node = old_array[i]
            while current_node is not None:
                temp_key = hash(current_node.key) % (old_capacity * 2 + 1)
                if new_array[temp_key] is not None:
                    temp_node = new_array[temp_key]
                    while temp_node.next is not None:
                        temp_node = temp_node.next
                    temp_node.next = current_node
                else:
                    new_array[temp_key] = current_node
                next_node = current_node.next
                current_node.next = None
                current_node = next_node

    new_key = hash(key) % dct.capacity

    if dct.array[new_key] is None:
        new_node = Node(key, value, None)
        dct.array[new_key] = new_node
        dct.size += 1
    else:
        current_node = dct.array[new_key]
        while current_node.key != key:
            if current_node.next is None:
                new_node = Node(key, value, None)
                current_node.next = new_node
                dct.size += 1
            current_node = current_node.next
        current_node.value = value


def remove(dct, key, default = None):
    """
    Remove a key and the value to which it maps.
    TODO: Implement this function. It must have O(1) complexity.

    :param dct: A Dictionary
    :param key: A hashable key to be removed
    :param default: A default value
    :return: The removed value, the default if the key does not exist
    """
    new_key = hash(key) % dct.capacity

    if dct.array[new_key] is None:
        return default
    if dct.array[new_key].key == key:
        current_node = dct.array[new_key]
        dct.array[new_key] = dct.array[new_key].next
    else:
        current_node = dct.array[new_key]
        while current_node.next is not None and current_node.next.key != key:
            current_node = current_node.next
        if current_node.next is None:
            return default
        temp = current_node.next
        current_node.next = current_node.next.next
        current_node = temp
    dct.size -= 1
    return current_node.value


def keys(dct):
    """
    Enumerate all of the keys in a dictionary.
    TODO: Implement this function. It must have O(n) complexity.

    :param dct: A dictionary
    :return: A new List of the dictionary's keys, in no particular order
    """
    new_list = lst.List()
    j = 0
    for i in range(0, dct.capacity):
        current_node = dct.array[i]
        while current_node is not None:
            lst.add(new_list, j, current_node.key)
            current_node = current_node.next
            j += 1

    return new_list