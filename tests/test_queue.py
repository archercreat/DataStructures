from unittest import TestCase

from queue import Queue

class BaseQueueTest(TestCase):
    q = Queue()

    def setUp(self):
        self.q.put(10)
        self.q.put('test')
        self.q.put(3)

    def tearDown(self):
        self.q.clear()

    def test_peek(self):
        self.assertEqual(self.q.peekLast(), 3)
        self.assertEqual(self.q.peekFirst(), 10)

    def test_put(self):
        var = 'testtesttest'
        self.q.put(var)
        self.assertEqual(self.q.peekLast(), var)
        self.assertEqual(self.q.get(), 10)
        self.assertEqual(self.q.get(), 'test')
