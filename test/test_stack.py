import unittest
from tdd_challenge.stack import Stack

class TestStack(unittest.TestCase):
    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty())


    def test_push_and_top(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(1, stack.top())


    def test_push_and_size(self):
        """スタックのサイズを取得"""
        stack = Stack()
        self.assertEqual(stack.size(), 1, "1 == 1")
