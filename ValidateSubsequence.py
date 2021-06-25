
def isValidSubsequence(array, sequence):
    newSequence = []
    i = 0
    while(i < len(array)):
        j = 0
        while(j < len(sequence)):
            print("array[i] = " + str(array[i]))
            print("sequence[j] = " + str(sequence[j]))
            if(array[i] == sequence[j]):
                temp = array[i]
                newSequence.append(temp)
                if(len(newSequence) > len(sequence)):
                    newSequence.pop(0)
                print(newSequence)
                i += 1
                j = 0
                if(i == len(array)):
                    break
            j += 1
        if(i == len(array)):
            break
        j = 0
        i += 1
    if(newSequence == sequence):
        print("array = " + str(array) + " Elements = " + str(len(array)))
        print("sequence = " + str(sequence) + " Elements = " + str(len(sequence)))
        print("subsequence = " + str(newSequence) + " Elements = " + str(len(newSequence)))
        return True
    else:
        print("array = " + str(array) + " Elements = " + str(len(array)))
        print("sequence = " + str(sequence) + " Elements = " + str(len(sequence)))
        print("subsequence = " + str(newSequence) + " Elements = " + str(len(newSequence)))
        return False

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

print(isValidSubsequence(array, sequence))