'''
tmercado:
Solution: 5/5
Big O: 5/5
tracing: 5/5
'''

from tree_node import *

def invert(root):

  def helper(root):
    if not root:
      return
      
    temp = root.left
    root.left = root.right
    root.right = temp

    helper(root.left)
    helper(root.right)
  helper(root)  

  return root
'''
time complexity: O(N) where n is the number of nodes in the tree because this solution goes through for each node in the tree until it is completed to invert the tree
space complexity: O(h) where h is the height of the tree because the space will depend on the recursive depth which in this case equals the height of the tree


Code tracing:

         7
       /   \
      4    8
     / \   
    1  2

Iterate through every node in the tree
first node =  7
we have a variable temp and make it equal to the left of the node
temp = 7.left = 4
and then we flip by making node.left = node.right and node.right = temp (which is the previous value of node)

next iteration (root.left) = helper(4)
temp = 4.left = 1
flip the left and right of 4
4.left = 4.right and 4.right = temp


next iteration (root.left) = helper(1)
since 1.left is none and 1.right is none, it basically just swaps none and then goes a step back

next iteration (root.right) = helper(2)
since 2.left is none and 2.right is none, it swaps none and goes a step back

next iteration (root.right) = helper(8) ***after it backs out of the other previous calls on the left sub tree
since 8.left and 8.right are both none, nothing is done

returns the root of the binary tree
'''
# node1 = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node5 = TreeNode(5)


# node1.left = node2
# node1.right = node3
# node2.left = node4
# node2.right = node5
# pretty_print(node1)
# invert(node1)
# print("-----------------------------------")
# pretty_print(node1)
