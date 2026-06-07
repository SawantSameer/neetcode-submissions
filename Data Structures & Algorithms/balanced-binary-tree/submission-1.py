class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            
            # Get left height. If it's -1, bubble up the failure.
            left = check(node.left)
            if left == -1: return -1
            
            # Get right height. If it's -1, bubble up the failure.
            right = check(node.right)
            if right == -1: return -1
            
            # If current node is unbalanced, return -1
            if abs(left - right) > 1:
                return -1
                
            # Otherwise, return actual height
            return max(left, right) + 1
            
        return check(root) != -1