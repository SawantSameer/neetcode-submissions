import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function that tracks the allowed range for the current node
        def validate(node, low=-math.inf, high=math.inf):
            # An empty node is technically a valid BST
            if not node:
                return True
            
            # If the current node's value falls outside the allowed range, it's invalid
            if node.val <= low or node.val >= high:
                return False
            
            # Recursively check the subtrees:
            # - For the left child, the max value it can be is the current node's value.
            # - For the right child, the min value it can be is the current node's value.
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))
        
        return validate(root)