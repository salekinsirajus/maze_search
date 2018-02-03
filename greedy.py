# Goal is to implement a greedy algorithm with a two dimensional list.
from transition import Tra_model
from heuristics import cartDist

def whileGreedy(graph, current, finish):
    t = Tra_model()
    path = [current] 
    # The order right, left, up, down is important
    while current != finish:
        try:
            right = t.move_right(current)
            left = t.move_left(current)
            up = t.move_up(current)
            down = t.move_down(current)
            
            # mapping these positions into a dictionary so we can
            # use the index obtained from the min() function below
            cells = {0:right, 1:left, 2:up, 3:down}
        except IndexError:
            # If we cannot
            # this part of the code is wrong
            print ("check if it actually exists in the graph")

        right_dist = cartDist(right, finish) 
        left_dist = cartDist(left, finish) 
        up_dist = cartDist(up, finish) 
        down_dist = cartDist(down, finish) 
        distances = [right_dist, left_dist, up_dist, down_dist]
        print (distances)
        closest = distances.index(min(distances))
        print ("The closest distance is: {0}".format(closest))
        current = cells[closest]
        path.append(current)
        print ("next stop is at: {0}".format(current))

    return path


if __name__ == '__main__':

    sample_graph = [
                     ['%','%','%','%','%','%'],
                     ['%', ' ', '%',' ', '.','%'],
                     ['%',' ', 'P',' ',' ', '%'], 
                     ['%','%','%','%','%','%']
                     ]

    print (whileGreedy(sample_graph, [1,1], [10,10]))
