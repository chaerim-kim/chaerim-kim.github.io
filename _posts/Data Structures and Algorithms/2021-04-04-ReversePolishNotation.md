---
title: "[Stack] Reverse Polish Notation - Python"
tags: [Data Structures and Algorithms]
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
Output: true
```

#### Example 2
```
Input: ["(1,2)", "(3,2)", "(2,12)", "(5,2)"] 
Output: false
```

## Code Implementation
- There are two rules:
  - Each child node has exactly one parent
  - Parent node can only have 2 children

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


## Explanation
1. First create and append a separate list for parent and child nodes
2. Based on the principal of 'Parent node can only have 2 children', this means that if there exists duplicating parent node, it'll be an illegal tree
3. All the children node should be unique; hence if there exists duplicate child node, return false.
