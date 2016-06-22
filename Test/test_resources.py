import unittest
from Models.Resources.linkedlist import *
from Models.Pieces.chesspiece import *


class LinkedListNodeTest(unittest.TestCase):
    def test_NodeNone(self):
        node = LinkedListNode(None, None, None)
        self.assertEqual(None, node.get_move_data())
        self.assertEqual(None, node.get_next())
        self.assertEqual(None, node.get_previous())

    def test_NodeMoveData(self):
        move = MoveData(Pawn(TeamColor.black, (3, 3)), Pawn(TeamColor.white, (4, 4)), TeamColor.white)
        node = LinkedListNode(None, None, move)
        self.assertEqual(move.get_piece1(), node.get_move_data().get_piece1())
        self.assertEqual(move.get_piece2(), node.get_move_data().get_piece2())
        self.assertEqual(move.get_turn(), node.get_move_data().get_turn())

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
        move_data = MoveData(Bishop(TeamColor.white, (4, 5)), Pawn(TeamColor.black, (3, 4)), TeamColor.white)
        node = LinkedListNode(None, None, move_data)
        linked_list.add_end(node)
        self.assertEqual(node, linked_list.get_last())
        self.assertEqual(node, linked_list.get_first())
        self.assertEqual(node, linked_list.get_current())
        self.assertEqual(None, linked_list.get_next())
        self.assertEqual(None, linked_list.get_previous())
        self.assertEqual(1, linked_list.get_count())
