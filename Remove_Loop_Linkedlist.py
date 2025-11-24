
'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''
#[Naive Approach] Detect and Remove Loop using Hashing - O(n) Time and O(n) Space
class Solution1:
    def removeLoop(self, head):
        nodeSet=set()
        prev=None
        while head != None:
            
            if head in nodeSet:
                prev.next=None
                return
            nodeSet.add(head)
            prev=head
            head=head.next
        



# Using Floyd's Cycle Detection Algorithm - O(n) Time and O(1) Space

class Solution:
    def removeLoop(self, head):
        # first we have to check the loop present or not in a Linkedlist 
        fast=head
        slow=head
         
        while fast!=None and fast.next!=None and slow!= None:
            fast=fast.next.next
            slow=slow.next
            if fast == slow:
                slow=head #reintialize the slow pointer
                # Move slow and fast pointers to find the node 
                # where the loop starts
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

            # Traverse the loop to find the node where the 
            # loop ends and remove it
                while fast.next != slow:
                    fast = fast.next
                fast.next = None     
                
        return True
            
       
        
        
        
        
        
        
        
        