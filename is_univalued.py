'''
tmercado:
Solution: 5/5
Big O: 3/5 - Is it log(n)? You have to hit every node to tell if all the values are the same right?
tracing: 5/5
'''
from tree_node import *

def is_univalued(root):

  def tree_helper(node,val):
    if not node:
      return True
    if node.val != val:
      return False
    return tree_helper(node.left,val) and tree_helper(node.right,val)

  val = root.val
  return tree_helper(root,val)
  

tree = TreeNode(5)
left = TreeNode(5)
right = TreeNode(5)
tree.left =  left
tree.right = right
print(is_univalued(tree))


'''
time complexity: the time complexity for this function will be O(logn) if the tree is balanced and O(n) for unbalanced trees where n is the number of nodes present in the tree
space complexity: O(h) where h is the height of the tree

code tracing:

        7
       /   \
      7    7
     / \   
    7  2

root = 7
tree_heper(7,7)

first iteration:
current node at the top(7)
if not node check: False
if node.val != val : False
since nothing was returned, it enters the return recursive call for left and right

node.right = 7
if node node check: False
if node.val != val: False
checks left and right of current node (7) and since both of them have values of None, it returns true for that side and returns back to parent node with a boolean value of true

node.left = 7 (node.left of root)
if not node check: False
if node.val != val: False
checks left and right of current node via the return recursive call

node.left = 7
if not node check: False
if node.val!= val: False
checks left and right of current node via the return recursive call
since both left and right of current node are None:
it returns true and comes back to this call 

node.right (7.right) = 2
if not node check: False
if node.val != val: True
returns False and exits to previous call

since the last node.right returns False,
every recursive call going back to the root will return False since
true AND false = False

when the call stack goes back to the beginning, it will then return False


    
'''