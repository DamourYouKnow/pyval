import unittest
from pyval import evaluate

class TestEvaluate(unittest.TestCase):
    def test_evaluate(self):
        self.assertEqual(evaluate("(2 + 3) * 5"), 25)
        self.assertEqual(evaluate("2 + 3 * 5"), 17)
        self.assertEqual(evaluate("(4 - 6) * ((4 - 2) * 2)"), -8)


if __name__ == '__main__':
    unittest.main()