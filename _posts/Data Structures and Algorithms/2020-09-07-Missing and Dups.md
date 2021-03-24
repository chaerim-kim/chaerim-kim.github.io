---
title: "Binary tree and List - Set Bits of a Binary Tree"
tags: [Data Structures and Algorithms, Binary Tree, List]
categories:
  - Data Structures and Algorithms
date: 2020-09-07
---


## Table of Contents
**Q:** Implement a function that counts the set bit of a binary tree in C.
1. [What is a Binary Tree?](#what-is-a-binary-tree)  
  1.1 [Binary Search Tree](#binary-search-tree)
2. [Steps and Pseudocode](#steps-and-pseudocode)  
  2.1 [Example](#example)  
  2.2 [Algorithm 1. Tree traversal](#algorithm-1-tree-traversal)  
  2.3 [Algorithm 2. Check set bits](#algorithm-2-check-set-bits)  
3. [Full Implementation](#full-implementation)   
4. [Test Cases](#test-cases)  


## What is a Binary Tree?
- A tree whose elements have at most 2 child nodes - the left and the right node.
- Nodes with no children are called 'leaves'.  
- The height h of a complete binary tree with N nodes is at most **O(log N)**.
  > - n = 1 + 2 + 4 + ... + 2<sup>h-1</sup> + 2<sup>h</sup> = 2<sup>h+1</sup> - 1
  > - Solving for h gives **O(log n)**


| Complete tree | Full Tree |
|-------------- | --------- |
| A tree that is completely filled, except for the bottom level, which is filled from left to right. | Binary tree in which each node has exactly zero or two children |
| ![Screenshot 2020-09-08 at 10 19 55 am](https://user-images.githubusercontent.com/33334078/92423656-d8b35b00-f1bc-11ea-8a2e-7f2c0be24907.png) | ![Screenshot 2020-09-08 at 10 20 08 am](https://user-images.githubusercontent.com/33334078/92423669-e072ff80-f1bc-11ea-8a8a-2786f6e10ff5.png) |


### Binary Search Tree
- Each node contains **one** key (also known as data)
- The **left nodes are less then the root node, and less than all of the right nodes**, in short L < P;
  - 10 > 6, 4, 8
  - To search a key in the tree, always compare it with the parent node - if key is smaller than parent, go to left. If larger, go to right.
- The keys in the **right subtree are greater the key in its parent node**, in short P < R;
  - 10 < 18, 15, 21
- ![image](https://user-images.githubusercontent.com/33334078/92438810-81c17c00-f1e4-11ea-8572-29d99837b1e5.png)




## Steps and Pseudocode
### Example  

| Input | Input in Binary | Result |  
| ----- | ------ | ------ |  
| ![1](https://user-images.githubusercontent.com/33334078/93730142-525a3880-fc02-11ea-956e-43fd025265b8.png) | ![2](https://user-images.githubusercontent.com/33334078/95733608-589d7b00-0cbd-11eb-85d4-d34ff5c6f1f4.png) | **8** (root: 2, left-subtree: 4, right-subtree: 2)|  
10,4,14,2,6 | 1010, 100,10,110,1110 | **9** (root: 2, left-subtree: 4, right-subtree: 3)|  



### Algorithm 1. Tree traversal
- **InOrder Traversal** : Left then root then right
- **PreOrder Traversal** : Root then left then right
- **PostOrder Traversal** : Left then right then root
- Here we use Pre-Order traversal - Traverse the tree from the root, to the left and the right sub-tree
- **Steps**
  1. Visit the root
  2. Traverse the left subtree  
  3. Traverse the right subtree



#### Code
```c
/* A binary tree node has data, pointer to left child and a pointer to right child */
struct node_t  { 
  uint8_t data; 
  struct node_t *left; 
  struct node_t  *right;
 }; 

void pre_order_traversal(struct node* root) {
  if (root != NULL)
    pre_order_traversal(root->left);
    pre_order_traversal(root->right);

```   




### Algorithm 2. Check set bits
- Check if the last bit is odd.
  - if odd then count++1
- Shift the bits to the right
- Shift until the end of the bits


#### Code
```c
int count_bits(struct node_t *n){
  uint8_t data = n->data; 
  int count = 0;

  // bc its unsigned int 8 hence 8 bits (1byte) (range = 0 to 255)
  for (int i = 0; i <= 8; i++){
    // check if last bit is odd ( bc its always +1)
    if (int i % 2 == 1) {
      count +=1
    }
    // then shift one bit
    i >> 1

    return count;
  }
```




## Full Implementation
 - The two functions have been merged to one function that is called recursively, to count the set bits and to traverse the right and left subtree.

```c
#include <stdio.h>
#include <stdlib.h>

struct node {
   uint8_t data;
   struct node *left;
   struct node *right;
};


struct node *root = NULL;

// Inserting data into the tree
void insert(int data) {
   struct node *tempNode = (struct node*) malloc(sizeof(struct node));
   struct node *current;
   struct node *parent;

   tempNode->data = data;
   tempNode->left = NULL;
   tempNode->right = NULL;

   //if tree is empty
   if(root == NULL) {
      root = tempNode;
   } else {
      current = root;
      parent = NULL;

      while(1) {
         parent = current;
         //go to left of the tree
         if(data < parent->data) {
            current = current->left;

            //insert to the left
            if(current == NULL) {
               parent->left = tempNode;
               return;
            }
         }  //go to right of the tree
         else {
            current = current->right;

            //insert to the right
            if(current == NULL) {
               parent->right = tempNode;
               return;
            }
         }
      }
   }
}


int pre_order_traversal(struct node* root) {
  // set the count variable for each subtree
  int root_count, left_count, right_count = 0;

  if (root == NULL) {
    return 0;
  }

  uint8_t data = root->data;
  int count = 0;
  // bc its unsigned int 8 hence 8 bits (1byte) (range = 0 to 255)
  while (data){
    // check if last bit is odd ( bc its always +1)
    if (data % 2 == 1) {
      count +=1;
    }
    // rightshift one bit
    data = data >> 1;
  }
    // Traverse Left Subtree
    left_count = pre_order_traversal(root->left);
    // Traverse Right Subtree
    right_count = pre_order_traversal(root->right);

  return count+left_count+right_count;
}


int main() {
  int i;

  // Test cases
  // int array[5] = { 10,6,18,4,8};
  // int array[5] = { 20,10,30,8,15};
  int array[5] = { 10,4,14,2,6};

  int count = 0;

  for(i = 0; i < 5; i++){
   insert(array[i]);
  }

  count = pre_order_traversal(root);
  printf("\nTotal set bits: %d \n", count);

	return 0;
}

```

## Test Cases
> **Input:** {10,6,18,4,8}  
> **Output:** 8

> **Input:** {10,4,14,2,6}  
> **Output:** 9

> **Input:** {20,10,30,8,15}  
> **Output:** 13

- Matches the Example test cases from 2.1.




### Key points
- Bit shifting  
- Tree insertion - [Reference link](https://www.tutorialspoint.com/data_structures_algorithms/tree_traversal_in_c.htm)
- Pre-order tree traversal
