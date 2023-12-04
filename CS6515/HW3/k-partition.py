import math
import statistics

def select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k-1]

    # Divide the input into groups of size 5
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    #print('k')
    #print(k)
    #print(groups)

    # Calculate the median of each group
    medians = [sorted(group)[len(group) // 2] for group in groups]

    #print(medians)

    # Recursively find the median of the medians
    pivot = select(medians, len(medians) // 2)

    #print('Pivot')
    #print(pivot)

    # Partition the input around the pivot
    smaller = [x for x in arr if x < pivot]
    larger = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    #print(smaller)
    #print(larger)
    #print(equal)

    if k <= len(smaller):
        #print("1st")
        return select(smaller, k)
    elif k > (len(smaller) + len(equal)):
        #print("2nd")
        return select(larger, k - len(smaller) - len(equal))
    else:
        #print("3rd")
        return pivot

def k_partition(arr, k):
    if k == 2:
        return select (arr, len(arr) // 2)
    
    partitions = []

    pivot = select (arr, len(arr) // 2)

    smaller = [x for x in arr if x <= pivot]
    larger = [x for x in arr if x > pivot]

    partitions.append(k_partition(smaller, k/2))
    partitions.append(pivot)
    partitions.append(k_partition(larger, k/2))

    return partitions

def main():
    """
    The main function
    """
    testArray1 = [1,2,3,4,5,6,6,7,8,9,10]
    testArray2 = [1,2,3,4,5,6,6,7,8,9]
    testArray3 = [1,1,2]
    testArray4 = [1,2,3,4,5,6,7,8,9,10,11,20,25,28,12,13,14,15,16,16,17]
    testArray5 = [1,2,2,3]
    testArray6 = [10,11,12,13,14,15,16,16,1,2,3,4,5,6,7,8,9]
    testArray7 = [-1, 2, 4, 1, 3, 0, 18, -3]
    testArray8 = [-1, 2, 4, 5, 6, 8, 10, 12, 15, 17, 18, 19, 20, 23, 25, 30]

    #print(median_of_medians(testArray3)) 
    #print(select(testArray4, len(testArray4) // 2))
    #print(statistics.median(testArray4))   
    #print(median_of_medians(testArray6))
    #print(select(testArray6, 4))
    #rint(statistics.median(testArray6)
    print(k_partition(testArray7, 2))   
    print(k_partition(testArray7, 4)) 
    print(k_partition(testArray8, 2))   
    print(k_partition(testArray8, 4)) 
    print(k_partition(testArray8, 8))   


if __name__ == '__main__':
    main()