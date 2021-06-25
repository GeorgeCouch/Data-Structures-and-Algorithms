# O(n^2) time | O(1) space
def twoNumberSumForLoops(array, targetSum):
    newArray = []
    appendToArray = False
    for i in range(len(array)):
        for j in range(len(array)):
            if(array[i] + array[j] == targetSum):
                temp1 = array[i]
                temp2 = array[j]
                appendToArray = True
    if(appendToArray):
        newArray.append(temp1)
        newArray.append(temp2)
    print(array)
    return newArray

array = [3,5,-4,8,11,1,-1,6]

print("O(n^2) ")
print(twoNumberSumForLoops(array, 10))

# O(n) time | O(n) space
def twoNumberSumHash(array, targetSum):
    arrayToHash = {}
    for i in array:
        sumAdder = targetSum - i
        if sumAdder in arrayToHash:
            print(array)
            print(arrayToHash)
            return [sumAdder, i]
        else:
            arrayToHash[i] = sumAdder
    print(array)
    print(arrayToHash)
    return[]

array = [3,5,-4,8,11,1,-1,6]

print("O(n) ")
print(twoNumberSumHash(array, 10))