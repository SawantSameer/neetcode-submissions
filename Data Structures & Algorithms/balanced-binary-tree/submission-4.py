class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            return (max(height(root.left),height(root.right))+1)

        def dfs(root):
            if not root: return True
            if abs(height(root.left)-height(root.right)) >1:    
                return False
                
            # else:
            #     return True
            return dfs(root.left) and dfs(root.right)
             
        #if not root:True
        return dfs(root)
        
        