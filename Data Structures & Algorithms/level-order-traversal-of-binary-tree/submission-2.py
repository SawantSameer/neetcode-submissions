# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        h = self.height(root)
        if h==0: return []
        res = [0]*h
        
        for k in range(h):
            res[k] = self.findKDist(root,k)
        return res
    def height(self,root):
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)

        return max(lh,rh)+1

    def findKDist(self,root,k):
        if root==None:return []

        if k==0: 
            return ([root.val])
        else:
            left = self.findKDist(root.left,k-1)
            right = self.findKDist(root.right,k-1)
            return left + right

