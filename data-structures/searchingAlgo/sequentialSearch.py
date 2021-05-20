array = [1,3,5,1,4,64,12,51,24,7,41,122]
def searchMethod1(array, x):
    metadata = {"comparisions": 0, "steps": 0}
    for value in array:
        metadata['comparisions'] += 1
        metadata['steps'] += 1
        if x == value:
            return (True, metadata)
    return (False, metadata)

def searchMethod2(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return True
    return False

def searchMethod3(array, x):
    return True if x in array else False

def searchMethod4(array, x):
    return x in array

##for i in [1,2, 51, 222]:
##    print(searchMethod1(array, i))
##    print(searchMethod2(array, i))
##    print(searchMethod3(array, i))
##    print(searchMethod4(array, i))


    
