---
title: "[LeetCode 릿코드] Add two numbers - 파이썬"
tags: [Data Structures and Algorithms, LeetCode]
categories:
  - Data Structures and Algorithms
---


## Problem Statement


## Example
```

```

```


```

## Code Implementation

```

```

## Explanation

``` Python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create one single node with value 0
        carry = 0
        l3 = ListNode(val = (l1.val + l2.val + carry) % 10)
        carry = (l1.val + l2.val) // 10
        curr = l3

        # run until each have the same length
        while l1.next != None and l2.next != None:
            l1 = l1.next
            l2 = l2.next

            curr.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (carry + l1.val+l2.val) //10
            curr = curr.next

        # break out if only l1 and l2 exists
        while l1.next:
            curr.next = ListNode((l1.val + carry) % 10)
            carry = (carry + l1.val) //10
            curr = curr.next

        while l2.next:
            curr.next = ListNode((l2.val + carry) % 10)
            carry = (carry + l2.val) //10
            curr = curr.next


        return l3

```
