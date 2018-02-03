from heuristics import manDist
from data_structures import PriorityQueue, listGraph
import copy
# A* = g + h
# g: cost so far
# h: heuristic.
# Not sure why this is more helpful
# come up with the g (cost so far) function and understand why would that be
# helpful in case of the same cost nodes.

# Need to use a priority queue

def aStarSP(graph, start, goal):
    '''A* search for single prize. 
    graph is a list of points. (e.g. [[1,3],[4,5],[7,5]]
    a point is a list of two integers (e.g. [1,3])
    start and goal are two points in the maze
    '''
    # convert the lists into tuple, lists are unhashble
    start_t = copy.deepcopy(start)
    start_t = tuple(start_t) 
    goal_t = copy.deepcopy(goal)
    goal_t = tuple(goal_t)
 
    print("start:{0}, start_t {1}".format(type(start), type(start_t)))
    print("goal:{0}, goal_t {1}".format(type(goal), type(goal_t)))
    # initialize an empty PQ
    explore_next = PriorityQueue()
    # Adding the start node to the the PQ. It has a priority of
    # cost being 0??
    explore_next.push(start, 0)
    # NEEDS TUPLE as data type
    cost_atm = {}
    # INSET TUPLE HERE
    cost_atm[start_t] = 0
    # TUPLE as data type
    predecessors = {}
    # INSERT TUPLE
    predecessors[start_t] = None
    

    while not explore_next.is_empty():
        # get the one with the smallest cost
        current_l = explore_next.pop()    # tuple
        current_t = copy.deepcopy(current_l)
        current_t = tuple(current_t)
        print (current_l, current_t)
        print("current_l:{0}, current_t {1}".format(type(current_l), type(current_t)))
        print ("BEFORE THE BREAK line")
        print (current_l, goal, type(current_l), type(goal))
        if current_l == goal:
            # go home, got the prize
            print ("found the prize! {}".format(cost_atm[current_t]))
            break
        for next in graph.neighbors(current_l):
            next_t = copy.deepcopy(next)
            next_t = tuple(next_t)
            print ("Where is the problem?")
            print("next:{0}, next_t {1}".format(type(next), type(next_t)))
            print ("{0}{1}{2}".format(cost_atm[current_t], current_l, next))
            new_cost = cost_atm[current_t] + graph.cost(current_l, next)

            if next_t not in cost_atm or new_cost < cost_atm[next_t]:
                cost_atm[next_t] = new_cost
                print (type(new_cost))
                print (manDist(next, goal), type(manDist(next, goal)))
                priority = new_cost + manDist(next, goal)
                explore_next.push(next, priority)
                predecessors[next_t] = current_t
    #print ("{0}".format( cost_atm, explore_next))
