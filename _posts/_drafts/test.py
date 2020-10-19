# Q2. Given an unsorted list with a missing number, write a function that finds the missing number in the list.

def find_missing(arr):
    arr_sum = 0
    full_sum = 0

    # find the sum of a given array
    for i in arr:
        arr_sum += i

    ## find the sum of a full array
    for j in range(0,len(arr)+1):
        full_sum += j

    print( full_sum - arr_sum)
    return full_sum - arr_sum


# find_missing([0,1,3,4,5]) # missing = 2



def find_duplicate(arr):
    arr_sum = 0
    full_sum = 0

    # find the sum of a given array
    for i in arr:
        arr_sum += i

    # find the original array sum
    for j in range(0, max(arr)+1):
        full_sum += j

    # finding duplicate by subtratcing the original (correct sum) from duplicated sum
    print( arr_sum - full_sum)
    return  arr_sum - full_sum


# find_duplicate([0,1,3,2,4,4,5])   # dup = 4



duplicateAndMissing =  [0, 5, 2, 6, 5, 1, 7, 3] # duplicate = 5, missing = 4
# duplicateAndMissing =  [0, 1, 4, 3, 3] # duplicate = 3, missing = 2


def find_missing_duplicates(duplicateAndMissing):
    missing = 0
    dup = 0

    duplicateAndMissing.sort()
    # print (duplicateAndMissing)
    for i in range(len(duplicateAndMissing)-1):
        if i != duplicateAndMissing[i]:
            missing = i
            dup = duplicateAndMissing[i]
            break

    print ("Missing: "+str(missing))
    print ("Duplicate: "+str(dup))
    return


find_missing_duplicates(duplicateAndMissing)
