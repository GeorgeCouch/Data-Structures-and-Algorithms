# O(nlogn) time | O(n) space
def sortedSquaredArrayUseSort(array):
    arridx = 0
    for value in array:
        temp = value**2
        array[arridx] = temp
        arridx += 1
    array.sort()
    return array

array = [1, 2, 3, 5, 6, 8, 9]
print(sortedSquaredArrayUseSort(array))

# O(n) time | O(n) space
def sortedSquaredArray(array):
    newArray = [0] * (len(array))
    startidx = 0
    endidx = len(array) - 1
    for value in reversed(range(len(array))):
        if abs(array[startidx]) < abs(array[endidx]):
            newArray[value] = abs(array[endidx])
            newArray[value] = newArray[value]**2
            endidx -= 1
        elif abs(array[startidx]) > abs(array[endidx]):
            newArray[value] = abs(array[startidx])
            newArray[value] = newArray[value]**2
            startidx += 1
        else:
            newArray[value] = array[startidx]
            newArray[value] = newArray[value]**2
            endidx -= 1
    return newArray
    
array = [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]
print(sortedSquaredArray(array))