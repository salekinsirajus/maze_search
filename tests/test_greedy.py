import unittest
from .. import greedy

class cartesianDistTest(unittest.TestCase):
    def testTwoEqual(self):
        self.assertEqual(greedy.heur_func([[1,1]],[[1,1]]), 0)

if __name__ == '__main__':
    unittest.main()
