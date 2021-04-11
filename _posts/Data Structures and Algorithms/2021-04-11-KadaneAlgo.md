---
title: "카데인 알고리즘 - Kadane's Algorithm maximum subarray"
tags: [Data Structures and Algorithms]
categories:
  - Data Structures and Algorithms
---


## Explanation
리스트에서 맥스 서브어레이를 찾을때, i (현재값)를 이전 인덱스가 가지고 있는 최대부분합과 비교해 더 큰값으로 바꾸는(replace) 알고리즘 입니다.

예시로 보는게 빠를것 같아요.

## Code Implementation
- 레인지가 1 인이유는, 값이 wrap 되어 어레이의 arr[0] 값과 arr[-1]가 계산되는 불상사가 발생하기 때문이다. 우리는 arr[i]값을 바꾸는 형태로
구현하기 때문에, arr[0]에 max값이 있어도, 괜찮다! 그게 맥스라면 그걸 아웃풋할테니. 
  
```python
def kadanealgo(arr):
    for i in range(1, len(arr)):
        # 바로 앞 숫자를 맥스 값으로 바꿈.
        arr[i] = max(arr[i], arr[i]+arr[i-1])
    return max(arr)
```


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


