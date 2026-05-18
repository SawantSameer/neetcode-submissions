# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# A SOLUTION WITHOUT USING THE DUMMY VARIBLE

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Handle initial empty list edge cases
        if not list1: return list2
        if not list2: return list1

        # 2. Determine the actual head of the merged list
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
            
        # 3. Setup our "current" pointer
        current = head

        # 4. NOW we can finally start the normal loop
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2

        return head