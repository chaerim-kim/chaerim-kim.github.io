---
title: "Array - Missing Number and Duplicates"
tags: [Data Structures and Algorithms, Array]
categories:
  - Data Structures and Algorithms
date: 2020-10-14
---



## Table of Contents
**Q:** Find a missing number and duplicates in a given array
1. [Find a missing number in a given array](#find-a-missing-number-in-a-given-array)  
 1.1 [Example](#example)     
 1.2 [Code Implementation](#code-implementation)  
2. [Find duplicates in a given array](#find-duplicates-in-a-given-array)  
  2.1 [Example](#example)     
  2.2 [Code Implementation](#code-implementation)
3. [Find a missing number and duplicates in a given array](#find-a-missing-number-and-duplicates-in-a-given-array)  
  3.1 [Example](#example)      
  3.2 [Code Implementation](#code-implementation)     
  3.3 [Time Complexity](#time-complexity)  
  3.4 [Space Complexity](#space-complexity)  


## Find a missing number in a given array
### Example

| Input | Output |
|-------|--------|
| [1, 4, 6, 2, 5, 7] | missing = 3 |
| [8, 4, 3, 2, 6, 7, 5] | missing = 1 |


### Code Implementation
- Uses the subtraction of the correct array sum and the given array sum to find the missing number.
- The sum of the correct array will always be greater, hence the full_sum - array_sum.

```python
def findMissing(arr):
    arr_sum = 0
    full_sum = 0

    # find the sum of a given array
    for i in arr:
        arr_sum += i

    # find the sum of a full array
    for j in range(0,len(arr)+1):
        full_sum += j

    print (full_sum - arr_sum)
    return full_sum - arr_sum
```



## Q2. Find duplicates in a given array
### Example

| Input | Output |
|-------|--------|
| [0, 1, 3, 2, 4, 4, 5]) | dup = 4 |
| [1, 8, 7, 4, 3, 2, 6, 7, 5] | dup = 7 |


### Code Implementation
- Also uses the subtraction between the correct array sum and the given array sum.
- This time, as the duplicated sum will be greater (due to the duplicated number), the subtraction is done the other way around.
- To find the original array sum, it finds the maximum of the array and uses that as a range for addition.

```python
def find_duplicate(arr):
    arr_sum = 0
    full_sum = 0

    # find the sum of a given array
    for i in arr:
        arr_sum += i

    # find the original array sum
    for j in range(0, max(arr)+1):
        full_sum += j

    # finding duplicate by subtracting the original (correct sum) from duplicated sum
    print (arr_sum - full_sum)
    return  arr_sum - full_sum
```




## Find a missing number and duplicates in a given array

### Example

| Input | Output |
|-------|--------|
| [1, 4, 2, 5, 4] |  missing = 3, repeated = 5 |
| [0, 5, 2, 6, 5, 1, 7, 3] | duplicate = 5, missing = 4 |


### Code Implementation
**Initial thoughts**
- *[Sorting & flagging] when there exists a missing number & repeated (comparison with sorted array)
  - Pro: Ease of implementation
  - Con: long running time, comparison taking time if the item is in the end of the array
- [Sets] to find missing
  - Con: it removes duplicates hence doesn't do its job


```python
duplicateAndMissing =  [0, 5, 2, 6, 5, 1, 7, 3] # duplicate = 5, missing = 4

def find_missing_duplicates(duplicateAndMissing):
    missing = 0
    dup = 0

    duplicateAndMissing.sort()
    for i in range(len(duplicateAndMissing)-1):
        if i != duplicateAndMissing[i]:
            missing = i
            dup = duplicateAndMissing[i]
            break

    print ("Missing: "+str(missing))
    print ("Duplicate: "+str(dup))
    return
```
### Time complexity
- variable declaration: O(1) * 2
- Python sort(): O(n log n)
- For and if loop:
  - For loop will execute n times, hence O(n)
  - The inner if condition, which is a comparison, is done in constant time, C.
  - Hence the for and if loop: O(n)
- = O(1) + O(nlogn)+ O(n). By the definition of the Big-O, the total time complexity is **O(nlogn)**.



### Space Complexity
- The space complexity needed for the above code would be:
> 4 * len(arr) = 4n bytes
> 4 * 3 bytes for variable missing, dup and i

- Hence the total memory required will be (4n+12), hence O(n) - in other words, a linear space complexity.
