

class Node(object):

    def __init__(self, value, next_=None):
        self._value = value
        self._next = next_

def flatten_linked_list(node):

    print(node)

if __name__ == '__main__':
    r1 = Node(1)  # 1 -> None - just one node
    print(r1._value)
    print(r1._next)
    r2 = Node(7, Node(2, Node(9)))  # 7 -> 2 -> 9 -> None
    # 3 -> (19 -> 25 -> None ) -> 12 -> None
    r3 = Node(3, Node(Node(19, Node(25)), Node(12)))
    r3_flattenned = flatten_linked_list(r3)  # 3 -> 19 -> 25 -> 12 -> None
    r3_expected_flattenned_collection = [3, 19, 25, 12]