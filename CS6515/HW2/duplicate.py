import math

def duplicate(numArray):
    """
    """
    print(numArray)
    # Base case
    if len(numArray) == 2:
        if numArray[0] == numArray[1]:
            return numArray[0]

    if (len(numArray) % 2 == 0):
        midpoint_position = int((len(numArray) / 2)) - 1
        midpoint_correct_value = numArray[0] + int(len(numArray) / 2) - 1
        #print(numArray[midpoint_position])
        #print(midpoint_correct_value)
        if (numArray[midpoint_position] == numArray[midpoint_position+1]):
            return numArray[midpoint_position]
        elif numArray[midpoint_position] == midpoint_correct_value:
            return duplicate(numArray[midpoint_position+1:])  
        else:
            return duplicate(numArray[0:midpoint_position+1])
    else:
        midpoint_position = math.floor(len(numArray) / 2)
        midpoint_correct_value = numArray[0] + math.floor(len(numArray) / 2)
        #print(midpoint_position)
        if (numArray[midpoint_position] == numArray[midpoint_position+1] or numArray[midpoint_position] == numArray[midpoint_position-1]):
            return numArray[midpoint_position]
        elif (numArray[midpoint_position] == midpoint_correct_value):
            print("check")
            return duplicate(numArray[midpoint_position+1:])   
        else:
            return duplicate(numArray[0:midpoint_position])

def main():
    """
    The main function
    """
    testArray1 = [1,2,3,4,5,6,6,7,8,9,10]
    testArray2 = [1,2,3,4,5,6,6,7,8,9]
    testArray3 = [1,1,2]
    testArray4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16]
    testArray5 = [1,2,2,3]
    testArray4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16]
    print(duplicate(testArray1))
    print(duplicate(testArray2))
    print(duplicate(testArray3))
    print(duplicate(testArray4))
    print(duplicate(testArray5))

if __name__ == '__main__':
    main()