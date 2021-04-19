---
title: "[Leetcode] 191. Number of 1 Bits (Python)"
tags:
  - Data Structures and Algorithms
  - Leetcode
  - Linked List
categories:
  - Data Structures and Algorithms
---

https://leetcode.com/problems/number-of-1-bits/

## Explanation
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
unsigned int 자료형에서 1의 갯수를 세서 리턴하는것. This is a bitwise ‘and’ operation.


## Example
#### Example 1
```
Input: n = 00000000000000000000000000001011
Output: 3
```

#### Example 2
```
Input: n = 00000000000000000000000010000000
Output: 1
```

## Implementation
1. Python built-in f(x)
   - can use bin() and count() to count the number of 1's
2. Modulo
   - for every least significant bit, we check if it is a 1 and increment if yes.
   - Then rightshift to continue 
3. Bitwise LeftShift
   - mask: mask is a number that has a 1 in the bit pos we want to check
   - at each step, we shift the mask by 1 and check if it is set. if 1, then increment
   - Big O: we increment 32 times. O(n*32) = O(n)
    
## Code Implementation

```python
def hammingWeight_strCount(self, n: int) -> int:
    return bin(n).count("1")
```

```python
def hammingWeight_mod(self, n: int) -> int:
    count = 0
    for i in range(32):
        if n % 2 == 1:
            count +=1
        n = n>>1
    return count

# checks in order of 11 -> 5 -> 2 -> 1 
```


```python
def hammingWeight_bitshift(n):
   # n is an unsigned 32 bit integer
    count = 0
    mask = 1
    for i in range(32):
        if n & mask != 0:
            count +=1
        mask <<= 1
    
    return count
```

```python
def hammingWeight_bitAND(n):
   # n is an unsigned 32 bit integer
    count = 0
    while n != 0:
        print(n)
        n = n & (n-1)       # eventually becomes 0, when no more shift bit left
        count +=1
    
    return count
```
