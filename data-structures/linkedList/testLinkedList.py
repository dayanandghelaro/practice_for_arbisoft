from linkedList import ValidationError, SNode, SLinkedList, DNode, DLinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    def test_SNode_initialization(self):
        self.assertRaises(TypeError, SNode, [])
        self.assertRaises(TypeError, SNode, True)
        self.assertRaises(TypeError, SNode, {})
        self.assertRaises(ValueError, SNode, None)
        
        
    def test_SLinkedList_initialization(self):
        self.assertRaises(TypeError, SLinkedList, "string")
        self.assertRaises(TypeError, SLinkedList, [])
        self.assertRaises(TypeError, SLinkedList, True)
        self.assertRaises(TypeError, SLinkedList, 123)
        head = SNode("First Node")
        linkedList = SLinkedList(head)
        self.assertAlmostEqual(linkedList.head.data, "First Node")
        self.assertAlmostEqual(linkedList.head.next, None)

    def test_addNode_SLinkedList(self):
        llist = SLinkedList()
        llist.addNodeAtStart("1")
        llist.addNodeAtEnd("2")
        llist.addNodeAtStart("3")
        self.assertAlmostEqual(llist.getSequence(), "3->1->2")
        

    def test_getSequence_SLinkedList(self):
        llist = SLinkedList()
        llist.addNodeAtStart("1")
        llist.addNodeAtStart("2")
        llist.addNodeAtStart("3")
        self.assertAlmostEqual(llist.getSequence(), "3->2->1")





    def test_DNode_initialization(self):
        self.assertRaises(TypeError, DNode, [])
        self.assertRaises(TypeError, DNode, True)
        self.assertRaises(TypeError, DNode, {})
        self.assertRaises(ValueError, DNode, None)
        
        
        

