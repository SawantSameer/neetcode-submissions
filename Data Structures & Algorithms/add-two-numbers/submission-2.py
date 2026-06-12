# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1,num2 = 0,0
        i = 0
        while l1:
            num1 = l1.val * (10**(i)) + num1
            i+=1
            l1 = l1.next
        j = 0
        while l2:
            num2 = l2.val * (10**(j)) + num2
            j+=1
            l2 = l2.next

        num = num1+num2
        dummy = ListNode()
        tail = dummy
        if num== 0:
            return ListNode(0)
        while num:
            tail.next = ListNode(num%10)
            num = num//10
            tail = tail.next

        return dummy.next