# Instructions

This homework assignment consists of four problems. For each problem, you need to:
- Attempt to solve the problem (spend no more than 30 minutes on each)
- Talk to a classmate. If you find yourself spending more than 30 minutes on a problem, consider asking a classmate, mentor, or instructor for help! If you can't solve a problem, be sure to submit any code you have for partial credit on the correctness portion of the grade.
  - If you use this second solution for the following questions, be sure to include it (you can name the function `*function_name*_second`) and credit your classmate in a comment

Then, **for each problem** choose whichever solution (yours or your classmate's) you think you can explain better and:
- Trace the code using a non-trivial instance of the problem - don't just run your code and print output, this must be done by hand (or typed). Include a picture or screenshot of your trace (you can upload images into your assignment from the **Files** menu above your .py files)
- State the time and space complexity of the solution, explaining your reasoning
  - This can be done in hw_questions.md

You should have 3 traces and 3 time+space complexity analyses.

Then, finally:
- Answer the remaining reflection questions in hw_questions.md

**Note: The TreeNode used in these problems is found in tree_node.py**

## Univalued Trees
A binary tree is *univalued* if and only if every node in the tree contains the same value. Write a function that receives the root of a binary tree as input and determines if the given tree is univalued. Feel free to write a helper (recursive) method.

Examples:
```
        7 
      /    \
    3      10           →  False
  /   \   /   \
-1    5   9    12

        5 
      /    \
     5      5           →  True

        7 
      /    \
    7       7           →  False
  /   \     / 
 7     7   8    

        3 
      /    \
    3      3           →  true
         /   \
        3     3
```

## Invert
Write a function that receives the root of a binary tree and inverts it. You should not create a new tree, just rearrange the nodes of the given one.

Example 1:
```
Tree (before method call)
        7 
      /    \  
    3      10           
  /  \     /  \
-1    5   9    12

Tree (after method call)

        7 
      /    \  
    10      3           
  /   \   /   \
12   9    5   -1
```
Example 2:
```
Tree (before method call)    
        2 
      /    \  
     3      1           

Tree (after method call)

        2 
      /   \  
     1      3   
```
Example 3:
```
Tree (before method call)                 
        7 
      /    \  
    3      10           
          /   \
         9    12

Tree (after method call)

        7 
      /    \  
    10      3           
  /   \
12     9
```

## Range Count
Write a method that receives the root of a **binary search tree** and returns the number of nodes with values between `min_val` and `max_val` (exclusive).

Examples:
```
        7 
      /    \
    3      10      
  /   \   /   \
-1    5   9    12

min_val = 2, max_val = 10  →  4
min_val = 3, max_val = 8  →  2
min_val = 10, max_val = 20  →  1
min_val = 20, max_val = 30  →  0
```