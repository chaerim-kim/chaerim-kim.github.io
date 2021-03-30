---
title: "[LeetCode 릿코드] Valid Parentheses - 파이썬"
tags: [Data Structures and Algorithms, LeetCode]
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

## Explanation
- 스트링의 char 하나하나 스캔하기
- 오픈 괄호라면, 스택에 밀어넣기
- 스택이 비어있거나, 새로운 캐릭터가 사전의 값과 같지 않으면, 리턴 폴스
- 스택이 비어있으면 트루 (다 매치돼서 나옴), 아니면 폴스
