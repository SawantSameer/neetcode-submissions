class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a true dummy node to start the merged list
        dummy = ListNode(-1)
        # 'current' will track the last node in our merged list
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            # Move the current pointer forward
            current = current.next
            
        # Once one list is empty, attach the remaining elements of the other list
        current.next = list1 if list1 else list2
        
        # Return the head of the merged list (skipping the dummy node)
        return dummy.next