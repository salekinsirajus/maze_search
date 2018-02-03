import unittest
from greedy import whileGreedy

#class cartesianDistTest(unittest.TestCase):
#    def testTwoEqual(self):
#        self.assertEqual(greedy.heur_func([[1,1]],[[1,1]]), 0)

class greedyAlgoTest(unittest.TestCase):
#    def __init__(self):
    graph = [[1,2],[2,2]]    

    def testSameStartFinish(self):
        self.assertEqual(whileGreedy(graph, [1,1], [1,1]), [[1,1]])

    def test2x2Diagonal(self):
        self.assertEqual(whileGreedy(graph, [1,1], [2,2]), [[1,1],[1,2],[2,2]])


if __name__ == '__main__':
    unittest.main()
