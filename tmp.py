import collections as c

eval_ = {'k1':10, 'k2':[[1,1],[2,4],[3,4],[1,3]]}
go = {'k1':10, 'k2':[[3,4],[1,3],[2,4],[1,2]]}

def eq_orderfree(list1, list2):
    """Check whether two lists contains the same elements regardless of the
       order. We convert the lists into tuple and then to set.
       use collections.Counter function
    """
    set1 = set(map(tuple, list1))
    set2 = set(map(tuple, list2))

    if c.Counter(set1) == c.Counter(set2):
        return True
    else:
        return False

# We need a mechanism for checking different type of values in the dictionary
# passed. The types we anticipate are: [a,b], [[1,2],[2,3]], 10. That is we
# will have to have mechanisms to evaluate equality of integers, 1-d list, and
# 2-d lists.

def goalTest(sample, ideal):
    """
    sample is the state we are wanting to examine. ideal is the goal state.
    """
    for goal in ideal:
        print ("goal in question is {}".format(goal))
        if isinstance (ideal[goal], int):
            print ("Within the try block")
            # for comparing integer
            if ideal[goal] != sample[goal]:
                print ("they int/single arrays are not matching")
                print (ideal[goal], sample[goal])
                return False
            else:
                print ("The int/list matched")
                pass
            # for comparing 2-d lists
        elif isinstance(ideal[goal], list):
            print ("There is a typeerror, mean it's a 2d list")
            print (ideal[goal], sample[goal])
            if eq_orderfree(ideal[goal], sample[goal]) != True:
                print ("Equality function returned false")
                print (ideal[goal], sample[goal])
                return False
            else:
                pass
                print ("Equality function returned true")
    print ("All things traversed. All goals are matched")
    return True

print (goalTest(eval_, go))
