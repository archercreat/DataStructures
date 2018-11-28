from unittest import TestCase

from LinkedList import LinkedList

class BaseListTest(TestCase):
    list = LinkedList()

    def setUp(self):
        self.list.add(10)
        self.list.add('test')
        self.list.add(3)

    def tearDown(self):
        self.list.clear()

    def test_size(self):
        self.assertEqual(self.list.size(), 3)
        self.list.add(1)
        self.list.add(2)
        self.assertEqual(self.list.size(), 5)

    def test_search(self):
        self.assertEqual(self.list.search(10), True)
        self.assertEqual(self.list.search(70), False)

    def test_remove(self):
        self.list.remove('test')
        self.assertEqual(self.list.size(), 2)
        self.assertEqual(self.list.head.data, 3)
        self.assertEqual(self.list.head.next.data, 10)
