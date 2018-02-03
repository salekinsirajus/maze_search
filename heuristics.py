import math

def cartDist(a, b):
    # a and b are two dimensional lists that looks like this:
    # a =[[5,4]], b = [[4,2]]
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]

    x = (x1 - x2) * (x1 - x2)
    y = (y1 - y2) * (y1 - y2)

    result = math.sqrt(x + y)
    print ("Heuristic function result: ", result)
    return result

def manDist(a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]

    x = abs(x1 - x2)
    y = abs(y1 - y2)

    print (x, y, x+y)
    result = x + y
    return result 
