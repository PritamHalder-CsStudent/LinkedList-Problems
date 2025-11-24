# Reverse the linked list 

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# using three pointer approach :
class Solution:
    def reverseList(self, head):
        prev=None
        curr=head
        while curr !=None:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        return prev    


# using recursive approach 
class Solution2:
    def reverseLL(self,head):
    # base case for single element
        if head == None or head.next==None:
            return head
        newHead=self.reverseLL(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newHead        