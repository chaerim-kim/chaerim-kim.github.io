# Q2. Given an unsorted list with a missing number, write a function that finds the missing number in the list.

def findMissing(arr):
    sum = 0
    ans = 0
    original = 0
    for i in arr:
        sum += i

    for j+1 in len(arr+1):
        original += j+1
