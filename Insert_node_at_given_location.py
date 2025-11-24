# Insert node at given position 

class Node:
    def __init__(self,val):
        self.data=val
        self.next=None


def insert_LinkedList(self, head,pos,value):
    if head==None:
        return 
    if pos<1:
        return head
    if pos==1: 
        newNode=Node(value)
        newNode.next=head
        head=newNode
        return head
    curr=head
    # Traverse to the node just before the new node
    for i in range(1,pos-1):
        if curr is None:
            return head
        curr=curr.next
    # If position is greater than number of nodes
    if curr is None:
        return head
    
    newNode=Node(value)
    # update the next pointers
    newNode.next=curr.next
    curr.next=newNode
    
    return head
    
                
        