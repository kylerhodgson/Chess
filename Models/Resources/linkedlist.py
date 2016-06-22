# Reinventing the wheel, just because I felt like getting some practice


class LinkedList:

    def __init__(self):
        self._baseNode = None
        self._first = None
        self._last = None
        self._current = None
        self._count = 0

    def add_end(self, node):
        if self._first is None:
            self._first = node
            self._last = node
            self._current = node
        else:
            node2 = self._last
            node2.set_next = node
            self._last = node
            self._current = node
        self._count += 1

    def add_next(self, node):
        if self._current is None:
            self._first = node
            self._last = node
            self._current = node
        elif self._current == self._last:
            self.add_end(node)
        else:
            node2 = self._current
            node2.set_next = node
            self._last = node
            self._current = node
        self._count += 1

    def get_count(self):
        return self._count

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

    def select_previous(self):
        self._current = self._current.get_previous()
        return self._current

    def select_next(self):
        if self._current == self._last:
            return None
        self._current = self._current.get_next()
        return self._current

    """TODO: make count always return the correct number of elements"""
    """TODO: do a lot of None checking"""


class LinkedListNode:

    def __init__(self, previous_node, next_node, move_data):
        self._previous = previous_node
        self._next = next_node
        self._move_data = move_data

    def get_previous(self):
        return self._previous

    def set_previous(self, node):
        self._previous = node

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node

    def get_move_data(self):
        return self._move_data


class MoveData:
    def __init__(self, piece1, piece2, turn):
        self._piece1 = piece1
        self._piece2 = piece2
        self._turn = turn

    def get_piece1(self):
        return self._piece1

    def get_piece2(self):
        return self._piece2

    def get_turn(self):
        return self._turn
