# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 

        # Finding the middle element
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        ptr = slow.next
        slow.next = None        # De-linking the list

        # Reversing the 2nd part of the LL

        head2 = None
        while ptr:
            temp = ptr.next
            ptr.next = head2
            head2 = ptr
            ptr = temp

        first, second = head, head2

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

        