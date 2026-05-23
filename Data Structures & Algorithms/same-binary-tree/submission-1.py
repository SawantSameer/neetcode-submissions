# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list_p=[]
        list_q=[]  
        self.dfs(p,list_p)
        self.dfs(q,list_q)

        return list_p==list_q

    def dfs(self,node,arr):
        if node!=None:
            arr.append(node.val)
            self.dfs(node.left,arr)
            self.dfs(node.right,arr)

        else:
            arr.append(None)

        
