array = [1,2,3,4,5,6,7,8,9,12,34,56,77,82,90]
def binarySearch(array, x):
    metadata = {"comparisions":0, "steps": 0}
    found = False
    minIndex, maxIndex = 0, len(array)
    while minIndex < maxIndex and not found:
        metadata['steps'] += 1
        mid = (minIndex+maxIndex)//2
        if array[mid] == x:
            metadata['comparisions'] += 1
            found = True
            break
        elif array[mid] < x:
            metadata['comparisions'] += 2
            minIndex = mid + 1
        else:
            metadata['comparisions'] += 2
            maxIndex = mid
    return found, metadata

def binaryRecursive(array, x, minIndex, maxIndex):
    mid = (minIndex+maxIndex)//2
    if array[mid] == x:
        return True
    elif minIndex == maxIndex:
        return False
    elif array[mid] > x:
        return binaryRecursive(array, x, minIndex, mid)
    else:
        return binaryRecursive(array, x, mid+1, maxIndex)

##for i in [-1,1,4, 7, 56, 90, 91]:
##    print('Iterative - ',i, '-',binarySearch(array, i))
##    print('Recursive - ', i, '-', binaryRecursive(array, i, 0, len(array)-1))
