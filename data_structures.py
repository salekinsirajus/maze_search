# Keep all the data structures we need for the program
import heapq

# graph from the 2-d list for faster navigation
class listGraph(object):
    '''listGraph object is used for better traversal of the 
        2d array for search algorithms with heuristics
    '''
    def __init__(self, list_2d):
        self.graph = list_2d
        self.wall = '%'
        self.prize = '.'
        self.empty = ' '
        self.visited = '#'
        # Should this be included?
        self.start = 'P'

    def is_valid_node(self, point):
        try:
            x = point[0]
            y = point[1]
            print ("type for point in is_valid_node ", type(point))
            print (point ,x, y)
            if self.graph[x][y]:
                # This is a valid point in the grid
                return True
        except IndexError:
            return False

    def cost(self, point_a, point_b):
        '''Is accurate only when two points are 
        neighbors. Returns the cost, or raise IndexError'''
        print("the points are: ", point_a, point_b)
        try:
            if self.is_valid_node(point_a):
                pass
            if self.graph[point_a[0]][point_a[1]] != self.wall:
                pass
        except IndexError:
            return IndexError

        neighbor_b = self.neighbors(point_b)
        print ("neighbors of b", neighbor_b)
        if point_a in neighbor_b:
            print ("cost from {0} to {1} is 1".format(point_a, point_b))
            return 1

        raise IndexError

    def neighbors(self, point):
        '''point is in the form of [1,3]
        Returns the neighboring cells that are traversible
        '''
        # Not sure if raising an IndexError is the best strategy
        if self.is_valid_node(point):
                pass
        else:
            raise IndexError    

        print ("the point we are trying to find neighbors for ", point)
        x = point[0]
        y = point[1]
        # row first, column second (opposite of cartesian)
        right = [x, y+1]
        left = [x, y-1]
        up = [x-1, y]
        down = [x+1, y]
        temp = [right, left, up, down]
        print ("neighboring cells are: ", temp)
        result = []
        for i, cell in enumerate (temp):
            print ("dealing with {0} at loop {1}".format(cell, i))
            try:
                if self.graph[cell[0]][cell[1]] != self.wall:
                   # not going to do anything with the popped value
                    print ("{0} is NOT a wall".format(cell))
                    result.append(temp[i])
#                else: 
#                    print ("{0} IS a wall".format(cell))
            except IndexError:
                pass
        return result
            

# Priority Queue
class PriorityQueue(object):
    '''Priority queue implemented with min heap (python's
    heapq data structure.
    '''
    def __init__(self):
        self.nodes = []
    
    def is_empty(self):
        if len(self.nodes) == 0:
            return True
        else:
            return False

    def push(self, node, priority):
        heapq.heappush(self.nodes, (priority, node))

    def pop(self):
        return heapq.heappop(self.nodes)[1]

    def show_queue(self):
        return self.nodes

