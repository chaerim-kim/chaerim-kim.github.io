---
title: "[Coderbyte] Reverse Polish Notation (Python)"
tags:   
  - Data Structures and Algorithms
  - Coderbyte
  - Stack
categories:
  - Data Structures and Algorithms
---


## Problem Statement
**Reverse Polish Notation**: It is a mathematical notation in which operators follow their operands. Watch this [video](https://www.youtube.com/watch?v=qN8LPIcY6K4) for more detailed explanation.

For example, given `3 4 + 2 * 1 +`, the operation would be: (3+4) *2 +1 = 15.
Whenever we see a number, we push to stack and if an operator, pop and perform the calculation and push it back to stack.



## Example
#### Example 1
```
Input: "3 4 + 2 * 1 +"
Output: 15
```

#### Example 2
```
Input: "3 5 + 7 2 – *"
Output: 40
```


## Explanation
1. Create a stack
2. When its a number, append to stack.
3. If it is an operation, pop and evaluate the statement, then pop back in


## Code Implementation

```python
def polish_eval(strArr):
    split_arr = strArr.split()
    stack = []

    for i in split_arr:
        if re.match ([\+\-\*\/], i):
            val2 = stack.pop()
            val1 = stack.pop()
						var = str(val1)+i+str(val2)
            stack.append(eval(var))
        else:
            stack.append(int(i))
    return stack[0]
```
