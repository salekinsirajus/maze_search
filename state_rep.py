#!/usr/bin/python

import sys


def parser(file):
    file_open = open (file, "r")
    big_list = []

    for line in file_open:
        line = line.strip("\n")
        line = list(line)
        big_list.append(line)

    return big_list
# In this part, we get a 2-D arry/list and extract some data
# about the 'world'
# example:
# 
# %%%%%%
# % % .%
# % P  %
# %%%%%%
parsed_array = [ 
                 ['%','%','%','%','%','%'],
                 ['%', ' ', '%',' ', '.','%'],
                 ['%',' ', 'P',' ',' ', '%'], 
                 ['%','%','%','%','%','%']
                ] 

def extractParams (array_2d):
    '''Given an array, this function extract
       the environment variables to make a representation of the world
    
       - # of prizes    
       - starting point (P)
       - prize locations (.)
    '''
    # do some checking (try?)
    # initialize with 0
    number_prizes = 0

    # Empty list of tuples
    prize_locations = []
    # starting point not found yet (default =  (-inf, -inf))
    # first index refers to line number
    # second index refers to char in the line
    starting_point = [-99999,-99999]

    for line in array_2d:
        for point in line:
            if point == '.':
                number_prizes += 1 
                print ("Addin these points ", array_2d.index(line),line.index(point))
                prize_locations.append([array_2d.index(line),line.index(point)])
            elif point == 'P':
                starting_point[0] = array_2d.index(line)
                starting_point[1] = line.index(point)
            else:
                pass
    print (number_prizes)
    print (starting_point)
    print (prize_locations)

def goalTest(eval_state, goal_state):
    # takes a state representation as an object
    # can be a dictionary (also the extractParams can return a dict)
    # There has to be a way to get the goals that are predefined 
    # and test those data against the passed argument
    #
    # arg_state = {'start': [1,1],'prizes':2,locations_prizes=[[1,2], [3,4]]}
    

def main():
    try:
        in_file = sys.argv[1]
        parsed = parser(in_file)
        extractParams(parsed)
    except IndexError as e:
        print ("Enter filename: python state_rep.py MAZE_FILENAME\n")
        exit
            
if __name__ == "__main__":
    main()

