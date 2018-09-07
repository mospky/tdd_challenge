import unittest
from tdd_challenge.add import Add


class TestAdd(unittest.TestCase):
    def test_add(self):
        add = Add()
        self.assertEqual(add.add(1, 2), 3, "3 == 3")
        self.assertEqual(add.add(7, 8), 15, "15 == 15")


if __name__ == '__main__':
    unittest.main()