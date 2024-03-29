---
title: "[Leetcode] 20. Valid Parentheses (Python)"
tags:
  - Data Structures and Algorithms
  - LeetCode
  - Stack
categories:
  - Data Structures and Algorithms
---


## Problem Statement
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.


## Example
#### Example 1
```
Input: s = "()"
Output: true
```

#### Example 2
```
Input: s = "([)]"
Output: false
```


## Explanation
1. 빈 스택을 정의합니다.
2. 스트링의 캐릭터를 하나하나 스캔하여, 오프닝 괄호면 스택에 밀어 넣습니다
3. 스택이 비어있거나, 새로운 캐릭터가 사전의 값과 같지 않으면, false를 리턴합니다.
4. 스택이 비어있으면 다 매치돼서 나온것이니 true를 리턴합니다.
(원래는 스택이 비어있지 않고 스택에서 뽑은게 현재와 일치하면 트루를 리턴했는데, 그러면 ']' 이경우에는 무조건 트루를 반환하게됨.그래서 생각을 바꿔서 스택이 비어있거나 (]} - 닫힌 괄호만 있거나), 뽑았을때 다른괄호인 경우는 폴스를 리턴하고, 그외엔 스택이 비면 트루, 아니면 폴스하게)


## Code Implementation

```Python
class Solution:
  def isValid(self, s: str) -> bool:
      stack = []
      dic = {'(':')',
             '{':'}',
             '[':']'
            }

      for char in s:
          if char in dic.keys():
              stack.append(char)

          elif stack == [] or char != dic[stack.pop()] :
              return False

      return stack ==[]
```
