'''
tmercado:
Solution: 5/5
Big O: 3/5 - is it worst case log(n)? What happens if the min value is lower than the lowest and max value is higher than the highest element.
tracing: 5/5
'''
from tree_node import *

def range_count(root, min_val, max_val):
  count = 0
  if not root:
    return 0
  if root.val > min_val and root.val < max_val:
    count +=1
  count += range_count(root.left,min_val,max_val)
  count += range_count(root.right,min_val,max_val)

  return count
  

'''
time complexity: for balanced trees, the time complexity of this function will be O(log n) whereas the worst case time for unbalanced trees will be O(n)
space complexity: worst case space scenario is O(h) where h is the height of the tree 

code tracing:

range_count(root,2,5)
min_val = 2
max_val = 5

        7
       /   \
      4    8
     / \   
    1  2
count = 0
starting at the root:
if not root: False
if root.valval > min value and < max value: False

recursive call ( count += range_count(root.left,min_val,max_val))

node.val = 4
if not root: False
if root.val > min and < max: True
count = 1
recursive call on .left and .right

node.val = 8
if not root: false
if root.val > min and < max: False
recursive call on .left and .right

since 8.left and 8.right are both none, it exits out of those stacks with 0

4.left = 1
node.val = 1
if not root: False
if root.val > min and < max: False

4.right = 2
node.val = 2
if not root: false
if root.val > min and < max: False
doesnt add to count

at the end of the function, count = 1 and therefore 1 is returned


'''
