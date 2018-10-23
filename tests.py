import unittest
from pyval import evaluate

class TestEvaluate(unittest.TestCase):
    def test_evaluate(self):
        self.assertEqual(evaluate("(2 + 3) * 5"), 25)
        self.assertEqual(evaluate("2 + 3 * 5"), 17)
        self.assertEqual(evaluate("(4 - 6) * ((4 - 2) * 2)"), -8)
        self.assertEqual(evaluate("(4 ** (2 + 1)) + (4 ** (2 + 1))"), 128)
        self.assertEqual(evaluate("10.5 - 1.4"), 9.1)


if __name__ == '__main__':
    unittest.main()