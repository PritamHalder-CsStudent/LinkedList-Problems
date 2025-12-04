'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

'''

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 # python ternary operator 
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry  # calulating sum 
            carry = total // 10        # carry calculation 
            curr.next = ListNode(total % 10) # result of sum operation 
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  

    
# val1 = l1.val if l1 else 0  means-->
# if l1 !=None:
#    val1=l1.val
# else:
#     val1=0
    