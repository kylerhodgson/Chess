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

    def get_count(self):
        return self._count

    def get_last(self):
        return self._last

    def get_previous(self):
        self._current = self._current.get_previous()
        return self._current

    def get_next(self):
        if self._current == self._last:
            return None
        self._current = self._current.get_next()
        return self._current


class LinkedListNode:

    def __init__(self, previous_node, next_node):
        self._previous = previous_node
        self._next = next_node

    def get_previous(self):
        return self._previous

    def set_previous(self, node):
        self._previous = node

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node
