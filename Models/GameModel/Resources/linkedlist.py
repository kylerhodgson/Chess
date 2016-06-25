# Reinventing the wheel, just because I felt like getting some practice


class LinkedList:

    def __init__(self):
        self._baseNode = None
        self._first = None
        self._last = None
        self._current = None
        self._count = 0
        self._current_index = -1

    def add_end(self, node):
        """Add to the end of the linked list
        Question: it sets the current node to the end node
        Did we want to keep this functionality, or leave current
        alone if it is different from the end value?
        """
        if self._current is None:
            self._first = node
            self._last = node
            self._current = node
        else:
            node2 = self._last
            node2.set_next(node)
            node.set_previous(node2)
            self._last = node
            self._current = node
        self._count += 1
        self._current_index = self._count - 1

    def add_next(self, node):
        if self._current is None or self._current == self._last:
            self.add_end(node)
        else:
            node2 = self._current
            node2.set_next = node
            self._last = node
            self._current = node
            self._current_index += 1
            self._count = self._current_index + 1

    def get_count(self):
        return self._count

    def get_current_index(self):
        return self._current_index

    def get_data(self):
        return self._current.get_data()

    def get_last(self):
        return self._last

    def get_first(self):
        return self._first

    def get_current(self):
        return self._current

    def get_previous(self):
        return self._current.get_previous()

    def get_next(self):
        return self._current.get_next()

    def has_next(self):
        return self._current.get_next() is not None

    def has_previous(self):
        return self._current.get_previous() is not None

    def move_previous(self):
        if self.has_previous():
            self._current = self._current.get_previous()
            self._current_index -= 1
            return True
        return False

    def move_next(self):
        if self.has_next():
            self._current = self._current.get_next()
            self._current_index += 1
            return True
        return False

    def move_to_index(self, index):
        if index < 0 or index >= self._count:
            return False
        while self._current_index != index:
            if index > self._current_index:
                self.move_next()
            else:
                self.move_previous()
        return True

    """TODO: make count always return the correct number of elements"""
    """TODO: do a lot of None checking"""


class LinkedListNode:

    def __init__(self, previous_node, next_node, data):
        self._previous = previous_node
        self._next = next_node
        self._data = data

    def get_previous(self):
        return self._previous

    def set_previous(self, node):
        self._previous = node

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node

    def get_data(self):
        return self._data


class MoveData:
    def __init__(self, old_piece1, old_piece2, new_piece1, new_piece2, old_turn, new_turn):
        self._old_piece1 = old_piece1
        self._new_piece1 = new_piece1
        self._old_piece2 = old_piece2
        self._new_piece2 = new_piece2
        self._old_turn = old_turn
        self._new_turn = new_turn

    def get_old_piece1(self):
        return self._old_piece1

    def get_new_piece1(self):
        return self._new_piece1

    def get_old_piece2(self):
        return self._old_piece2

    def get_new_piece2(self):
        return self._new_piece2

    def get_old_turn(self):
        return self._old_turn

    def get_new_turn(self):
        return self._new_turn
