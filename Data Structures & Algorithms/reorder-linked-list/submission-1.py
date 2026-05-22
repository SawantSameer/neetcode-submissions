# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        # 1. Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Sever the two halves
        l1 = head
        l2 = slow.next
        slow.next = None  # Cut the list in half to prevent cycles

        # 3. Reverse the second half
        curr = l2
        prev = None    
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l2 = prev

        # 4. Merge the two halves
        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next
            
            l1.next = l2
            l2.next = temp1
            
            l1 = temp1
            l2 = temp2  # Move l2 forward