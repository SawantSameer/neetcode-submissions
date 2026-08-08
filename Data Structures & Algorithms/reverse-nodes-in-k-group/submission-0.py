# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        n = len(nodes)
        
        def Rvrse(l, r):
            while l<r:
                nodes[l], nodes[r] = nodes[r], nodes[l]
                l+=1
                r-=1
        for i in range(n//k):
            Rvrse(k*i, k*(i+1)-1)

        for j in range(1, n):
            nodes[j-1].next = nodes[j]
        nodes[-1].next = None
        return nodes[0]
