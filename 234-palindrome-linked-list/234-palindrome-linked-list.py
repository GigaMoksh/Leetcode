# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        num = str(head.val)
        
        while head.next != None:
            num += str(head.next.val)
            head = head.next
            
        if num == num[::-1]:
            return True
        
        return False