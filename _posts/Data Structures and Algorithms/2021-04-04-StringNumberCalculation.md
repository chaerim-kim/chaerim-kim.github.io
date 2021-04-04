---
title: "[String] String Number Calculation - convert word to integer"
tags: [Data Structures and Algorithms]
categories:
  - Data Structures and Algorithms
---


## Problem Statement
Given a string strParam with numeric words, perform the calculation and return value as a string. if the value is <=0, say negative xx.


## Example
#### Example 1
```
Input: strParam = "oneminustwozero"    # 1-20 = -19
Output: negativeonenine
```

#### Example 2
```
Input: strParam = "oneminustwozeroplusthreetwo"    # 1-29+32 = 13
Output: onethree
```

## Code Implementation

```python
def stringtoNo(strParam):
    dict = {'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero': '0',
            'plus': '+',
            'minus': '-'}

    for i,j in dict.items():
        strParam = strParam.replace(i,j)

    # perform calculation
    result = eval(strParam)

    # convert back to string
    if result <= 0:
        result = str(result).replace('-', 'negative')

    for i,j in dict.items():
        result = str(result).replace(j, i)
    return result

print(stringtoNo('oneminustwozeroplusthreetwo'))    #onethree = 13
```

## Explanation
1. First replace the string using dictionary
2. Using eval() calculate the output of the equation
3. If its a negative number, replace - to negative
4. Using the dictionary, replace it back to string
