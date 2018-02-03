def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    explore_next = PriorityQueue()
    explore_next.put(start, 0)
    predecessors = {}
    visited_w_cost = {}
    predecessors[start] = None
    visited_w_cost[start] = 0
    
    while not explore_next.empty():
        current = explore_next.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = visited_w_cost[current] + graph.cost(current, next)
            if next not in visited_w_cost or new_cost < cost_so_far[next]:
                visited_w_cost[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                explore_next.put(next, priority)
                predecessors[next] = current
    
    return predecessors, visited_w_cost

