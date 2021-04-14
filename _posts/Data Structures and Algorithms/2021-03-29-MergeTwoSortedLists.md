---
title: "[Linked List] 21. Merge Two Sorted Lists (Python)"
tags:
  - Data Structures and Algorithms
  - LeetCode
  - Linked List
categories:
  - Data Structures and Algorithms
---

## Problem Statement
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.


## Example
~~~
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
~~~

~~~
Input: l1 = [], l2 = []
Output: []
~~~


## Explanation

1. 먼저 새로운 리스트 l3의 헤드인 `l3head`와 포인터인 `curr`을 선언해줍니다. 새로운 노드에는 0의 값이 들어가도록 선언합니다.

2. l1 과 l2의 값이 있는한, l1과 l2의 값을 비교합니다. l2의 값이 더 크다면, 현재의 포인터를 l1으로 지정하고, l1의 다음 노드로 넘어갑니다.

3. l1의 값이 더 큰 경우, l1, l2의 값이 같을 경우 등을 else문에서 처리하고, curr포인터가 다음을 가르킬수 있도록 `curr = curr.next` 를 선언합니다.

4. 두 배열의 길이가 다를경우, l1 또는 l2가 남았을때, 그 배열로 포인터를 지정해주고, 처음 선언했던 헤드노드의 넥스트 포인터를 리턴하며 종료합니다. (처음 선언한 l3head에는 0이 들어있기 때문)



이상입니다!


## Code Implementation

```Python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
l3head = curr = ListNode(0)

while l1 and l2:
    if l1.val < l2.val:
        curr.next = l1
        l1 = l1.next
    else:
        curr.next = l2
        l2 = l2.next
    curr = curr.next
curr.next = l1 or l2

return l3head.next
```
