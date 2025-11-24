# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# list1 and list2 are the head of the linkedlist 
class Solution:
    def mergeTwoLists(self, list1, list2 ):
        dummy=ListNode(0)  # create a dummy linkedlist take a temp pointer to point head of dummy linked list
        temp=dummy         #  this will help to store node at this dummy linkedlist
        p1=list1
        p2=list2
        while p1!=None and p2!=None:
            if p1.val<=p2.val:
                temp.next=p1
                p1=p1.next
            else:
                temp.next=p2
                p2=p2.next
            temp=temp.next    

        if p1 !=None:
            temp.next=p1
            p1=p1.next
        if p2!=None:
            temp.next=p2
            p2=p2.next
        return dummy.next