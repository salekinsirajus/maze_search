import copy

class Tra_model:

    def move_right(self, pointer):  #Move the pointer to the right
        current = copy.deepcopy(pointer)
        while True:
            try:
                current[1] += 1
                return current   #Increment one to the column
                break
            except IndexError:
                print("IndexError")
                break


    def move_left(self, pointer):    #Move the pointer to the left
        current = copy.deepcopy(pointer)
        while True:
            try:
                current[1] -= 1
                return current  #decrease one from the column
                break

            except IndexError:
                print("IndexError")
                break

    def move_up(self, pointer):         #Move the pointer up
        current = copy.deepcopy(pointer)
        while True:
            try:
                current [0] -= 1
                return current    #Add one to the row
                break

            except IndexError:
                print("IndexError")
                break

    def move_down(self, pointer):           #Move the pointer up
        current = copy.deepcopy(pointer)
        while True:
            try:
                current[0] += 1
                return current  #subtract one from the row
                break

            except IndexError:
                print("IndexError")
                break

'''
if __name__ == "__main__":
    init = [[6],[7]]
    t = TransModel(init)
    
    curr = [[1],[1]]
    t1 = t.move_right(curr)
    print ("curr ", curr)
    print ("t1", t1)
    t2 = t.move_right(curr)
    print ("curr", curr)
    print ("t2", t2)
'''
