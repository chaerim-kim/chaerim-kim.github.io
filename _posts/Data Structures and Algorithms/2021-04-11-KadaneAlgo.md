---
title: "[Leetcode] 53. Maximum Subarray - Kadane's Algorithm 카데인 알고리즘 (Python)"
tags:
  - Data Structures and Algorithms
  - Leetcode
  - Array
categories:
  - Data Structures and Algorithms
---


## Problem
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


## Explanation

#### 방법 1 - 리스트 내부의 값을 변경해서 max리턴하기
리스트에서 합이 가장큰 연속적인 서브리스트를 찾을때, i (현재값)를 이전 인덱스가 가지고 있는 최대부분합과 비교해 더 큰값으로 바꾸는(replace) 알고리즘 입니다. 이 설명은 밑에 예제에 있습니다.


#### 방법 2 - 변수 2개에 각각 로컬, 글로벌 max저장하기
로컬 맥스 + 현재값을 더했을때의 값과 현재값을 비교합니다. 글로벌은 이제까지의 맥스와 로컬 맥스를 비교하여 저장합니다.
![IMG_8366](https://user-images.githubusercontent.com/33334078/114655290-e3236d80-9d26-11eb-847f-4f784067b5cf.jpg)


## Example
#### Example 1
```
Input: [-1,4,-3,5,2]
Output: 8
```

i값 | max(현재 i값, 앞의 maxsum) |  현재 array
--- | --- |  ---
1 | max(4, 3)  # 4-1 | [-1,4,-3,5,2]
2 | max(-3, 1)  # 4+(-3) | [-1,4,`1`,5,2]
3 | max(5, 6)  # 5+1 | [-1,4,1,`6`,2]
4 | max(2, 8)  # 2+6 | [-1,4,1,6,`8`]
return | max(arr) = 8 | [4,-3,5,2]


#### Example 2
```
Input: [8,-10,5,2,1]
Output: 8
```

i값 | max(현재 i값, 앞의 maxsum) |  현재 array
--- | --- |  ---
1 | max(-10, -2)  | [8, `-2`, 5, 2, 1]
2 | max(5, -2)  | [8, -2, `5`, 2, 1]
3 | max(2, 7)   | [8, -2, 5, `7`, 1]
4 | max(1, 8)  | [8, -2, 5, 7, `8`]
return | max(arr) = 8 | [8]


## Code Implementation


#### 방법 1
- 레인지가 1 인이유는, 값이 wrap 되어 어레이의 arr[0] 값과 arr[-1]가 계산되는 불상사가 발생하기 때문이다. 우리는 arr[i]값을 바꾸는 형태로
구현하기 때문에, arr[0]에 max값이 있어도, 괜찮다! 그게 맥스라면 그걸 아웃풋할테니.

```python
def kadanealgo(arr):
    for i in range(1, len(arr)):
        # 바로 앞 숫자를 맥스 값으로 바꿈.
        arr[i] = max(arr[i], arr[i]+arr[i-1])
    return max(arr)
```


#### 방법 2
```python
def kadanealgo(arr):
  localmax = globalmax = 0

  for i in range(len(arr)):
      # localmax는 자기 자신과, 이제까지의 최대값 + 자기자신
      localmax = max(arr[i], localmax + arr[i])
      globalmax = max(localmax, globalmax)
      # print(localmax, globalmax)
  return globalmax
```
