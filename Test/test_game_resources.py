import unittest

from Models.GameModel.Resources.linkedlist import *
from Models.GameModel.Pieces.chesspiece import *


class LinkedListNodeTest(unittest.TestCase):
    def test_NodeNone(self):
        node = LinkedListNode(None, None, None)
        self.assertEqual(None, node.get_data())
        self.assertEqual(None, node.get_next())
        self.assertEqual(None, node.get_previous())

    def test_NodeMoveData(self):
        move = MoveData(Pawn(TeamColor.black, (3, 3)), Pawn(TeamColor.white, (4, 4)), None, None, TeamColor.white, None)
        node = LinkedListNode(None, None, move)
        self.assertEqual(move.get_old_piece1(), node.get_data().get_old_piece1())
        self.assertEqual(move.get_old_piece2(), node.get_data().get_old_piece2())
        self.assertEqual(move.get_old_turn(), node.get_data().get_old_turn())

    def test_NodeNext(self):
        node1 = LinkedListNode(None, None, None)
        node2 = LinkedListNode(None, node1, None)
        self.assertEqual(node1, node2.get_next())


class LinkedListTest(unittest.TestCase):
    def test_LinkedListNone(self):
        linked_list = LinkedList()
        self.assertEqual(None, linked_list.get_last())
        self.assertEqual(None, linked_list.get_first())

    def test_LinkedListAddEnd(self):
        linked_list = LinkedList()
        move_data = MoveData(None, None, None, None, None, None)
        node = LinkedListNode(None, None, move_data)
        linked_list.add_end(node)
        self.assertEqual(node, linked_list.get_last())
        self.assertEqual(node, linked_list.get_first())
        self.assertEqual(node, linked_list.get_current())
        self.assertEqual(None, linked_list.get_next())
        self.assertEqual(None, linked_list.get_previous())
        self.assertEqual(False, linked_list.move_next())
        self.assertEqual(False, linked_list.move_previous())
        self.assertEqual(1, linked_list.get_count())

    def test_LinkedListAddEndSeveral(self):
        linked_list = LinkedList()
        for i in range(10):
            linked_list.add_end(LinkedListNode(None, None, None))
        self.assertEqual(10, linked_list.get_count())
        self.assertTrue(linked_list.has_previous())
        self.assertFalse(linked_list.has_next())
        for i in range(9):
            self.assertTrue(linked_list.move_previous())

    def test_LinkedListIndexAndCount(self):
        linked_list = LinkedList()
        for i in range(40):
            linked_list.add_next(LinkedListNode(None, None, None))
            self.assertEqual(i + 1, linked_list.get_count())
            self.assertEqual(i, linked_list.get_current_index())
        for j in range(30):
            self.assertEqual(40, linked_list.get_count())
            self.assertEqual(39 - j, linked_list.get_current_index())
            linked_list.move_previous()
        for i in range(10):
            linked_list.add_next(LinkedListNode(None, None, None))
            self.assertEqual(11 + i, linked_list.get_count())
            self.assertEqual(10 + i, linked_list.get_current_index())
        linked_list.move_previous()
        self.assertEqual(18, linked_list.get_current_index())
        linked_list.add_end(LinkedListNode(None, None, None))
        self.assertEqual(21, linked_list.get_count())
        self.assertEqual(20, linked_list.get_current_index())
        self.assertFalse(linked_list.move_next())
