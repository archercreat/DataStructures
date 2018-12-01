from unittest import TestCase

from binaryTree import *

class BaseListTest(TestCase):
    tree = BinaryTree()

    def setUp(self):
    	self.tree.add(50)
    	self.tree.add(45)
    	self.tree.add(46)
    	self.tree.add(40)
    	self.tree.add(30)
    	self.tree.add(35)
    	self.tree.add(34)
    	self.tree.add(36)
    	self.tree.add(60)
    	self.tree.add(70)
    	self.tree.add(15)
    	self.tree.add(14)
    	self.tree.add(55)
    	self.tree.add(54)
    	self.tree.add(56)
    	self.tree.add(53)
    	self.tree.add(57)
    	self.tree.add(80)
    	self.tree.add(90)

    def tearDown(self):
        del self.tree.root

    def test_basecase(self):
        self.assertNotEqual(self.tree.search(50), None)
        self.assertNotEqual(self.tree.search(45), None)
        self.assertNotEqual(self.tree.search(46), None)
        self.assertNotEqual(self.tree.search(40), None)
        self.assertNotEqual(self.tree.search(35), None)
        self.assertNotEqual(self.tree.search(34), None)
        self.assertNotEqual(self.tree.search(36), None)
        self.assertNotEqual(self.tree.search(60), None)
        self.assertNotEqual(self.tree.search(70), None)
        self.assertNotEqual(self.tree.search(15), None)
        self.assertNotEqual(self.tree.search(14), None)
        self.assertNotEqual(self.tree.search(55), None)
        self.assertNotEqual(self.tree.search(54), None)
        self.assertNotEqual(self.tree.search(56), None)
        self.assertNotEqual(self.tree.search(53), None)
        self.assertNotEqual(self.tree.search(57), None)
        self.assertNotEqual(self.tree.search(80), None)
        self.assertNotEqual(self.tree.search(90), None)

    def test_2childsDelete(self):
        self.tree.delete(30)
        parent = self.tree.root.left.left
        self.assertEqual(self.tree.search(30), None)
        self.assertEqual(parent.left.data, 34)
        self.assertEqual(parent.left.left.parent, parent.left)
        self.assertEqual(parent.left.right.data, 35)
        self.assertEqual(parent.left.right.left, None)
        self.assertEqual(parent.left.parent, parent)

    def test_0childsDelete(self):
        self.tree.delete(14)
        min = self.tree.min(self.tree.root)
        self.assertEqual(self.tree.search(14), None)
        self.assertEqual(min.data, 15)
        self.assertEqual(min.left, None)

    def test_1childDelete(self):
        self.tree.delete(15)
        self.tree.delete(56)
        min = self.tree.min(self.tree.root)
        ff = self.tree.root.right.left

        self.assertEqual(self.tree.search(15), None)
        self.assertEqual(min.data, 14)
        self.assertEqual(min.parent.left, min)

        self.assertEqual(self.tree.search(56), None)
        self.assertEqual(ff.data, 55)
        self.assertEqual(ff.right.data, 57)
        self.assertEqual(ff.right.parent, ff)
