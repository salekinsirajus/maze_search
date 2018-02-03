f = [[1,2]]
x = 0 
y = 0

try:
    if f[x][y]:
        print ("there is a value that is not 0 or None")
    else:
        print ("Does not evaluate to true")

except IndexError:
    print (IndexError)
