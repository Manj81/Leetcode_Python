# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = l1.val + l2.val
        carry = sum // 10
        l3 = ListNode(sum%10)
        
        n1 = l1.next
        n2 = l2.next
        n3 = l3
        
        while n1 and n2:
            sum = carry + n1.val + n2.val
            carry = sum // 10
            n3.next = ListNode(sum%10)
            n3 = n3.next
            n1 = n1.next
            n2 = n2.next
            
        while n1:
            sum = carry + n1.val
            carry = sum // 10
            n3.next = ListNode(sum%10)
            n3 = n3.next
            n1 = n1.next
            
        while n2:
            sum = carry + n2.val
            carry = sum // 10
            n3 = n3.next
            n2 = n2.next
            
        if carry > 0:
            n3.next = ListNode(carry)
            
        return l3