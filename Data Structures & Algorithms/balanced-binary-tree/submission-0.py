# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            return max(lh, rh) + 1

        BF = 0
        
        def dfs(node):
            nonlocal BF  # Tell Python to use the BF variable from the outer function
            
            if node:
                # Calculate balance for this node
                current_balance = abs(height(node.left) - height(node.right))
                BF = max(BF, current_balance)
                
                # Continue down the tree
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return BF <= 1