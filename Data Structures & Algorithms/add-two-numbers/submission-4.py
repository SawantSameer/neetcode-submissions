# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = 0, 0
        i = 0
        while l1:
            num1 = l1.val * 10**i + num1
            i+=1
            l1 = l1.next
        #return ListNode(num1)
        i = 0
        while l2:
            num2 = l2.val * 10**i + num2
            l2 = l2.next
            i+=1

        value = num1 + num2
        res = []
        if not value: return ListNode(0)
        while value:
            res.append(value%10)
            value = value // 10
        head = ListNode(res[0])
        cur = head
        for i in range(1, len(res)):
            cur.next = ListNode(res[i])
            cur = cur.next

        return head
