import unittest

from main import execute_challenge


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_something():
        execute_challenge()
        # self.assertEqual(10, 10)


if __name__ == '__main__':
    unittest.main()
