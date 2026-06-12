# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        p,q = list1,list2
        while p:
            res.append(p.val)
            p = p.next
        while q:
            res.append(q.val)
            q = q.next
        res.sort()
        if not res:
            return None
        head = ListNode(res[0])
        curr = head
        for x in res[1:]:
            curr.next = ListNode(x)
            curr = curr.next

        return head