from data_structures import listGraph
from state_rep import parser
from aStar import aStarSP
import sys

if __name__ == '__main__':
    infile = sys.argv[1]
    parsed = parser(infile)
    
    g = listGraph(parsed)

    aStarSP(g, [1,1], [10,12])
