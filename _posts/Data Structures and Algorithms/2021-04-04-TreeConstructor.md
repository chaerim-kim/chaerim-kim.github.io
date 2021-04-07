---
title: "[Binary Tree, Array] Tree Constructor - Python"
tags: [Data Structures and Algorithms]
categories:
  - Data Structures and Algorithms
---


## Problem Statement
TreeConstructor(strArr) take the array of strings stored in **strArr**, which will contain pairs of integers in the following format: **(i1,i2),** where i1 is child node and i2 represents the parent node.

If strArr can form a proper binary tree, return true. If not, return false.
![img](https://i.imgur.com/NMRdSO1.png)


## Example
#### Example 1
```
Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"] 
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
def TreeConstructor(strArr):
    parent = []
    child = []

    for i in strArr:
        child.append(int(i[1]))
        parent.append(int(i[3]))
    # each parent node have at most 2 children
    for k,v in Counter(parent).items():
        if v > 2:
            return False
    # each node is unique
    for k,v in Counter(child).items():
        if v > 1:
            return False
    return True

print (TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))      # True
print (TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"] ))      # False
```


## Explanation
1. First create and append a separate list for parent and child nodes
2. Based on the principal of 'Parent node can only have 2 children', this means that if there exists duplicating parent node, it'll be an illegal tree
3. All the children node should be unique; hence if there exists duplicate child node, return false.
