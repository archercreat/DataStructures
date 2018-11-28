from unittest import TestCase

from stack import Stack

class BaseStackTest(TestCase):
    stack = Stack()

    def setUp(self):
        self.stack.push(10)
        self.stack.push('test')
        self.stack.push(3)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 'test')
        self.assertEqual(self.stack.pop(), 10)
