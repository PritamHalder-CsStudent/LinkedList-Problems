'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

# Using two pointer Approach : Hare-turtle method 
# Hare(Fast) pointer will jump two step and Turtle(slow) pointer will jump one step , 
# if loop present at a sertain time Fast and slow pointer will meet then we can detect Linkedlist contain loop.

class Solution:
    def detectLoop(self, head):
        fast=head
        slow=head
        
        while fast!=None and fast.next!=None and slow!= None:
            fast=fast.next.next
            slow=slow.next
            if fast == slow:
                return True
                break
        
        return False        
                
        
        
