# create a node object that will contain value and next pointer . 
# next pointer will point to other node to create a Linkedlist.

# node creation 
class Node:
    def __init__(self,data):              # python constractor 
        self.value=data     # initailize the value of node 
        self.next=None      # next pointer should be none 
      
# a=Node(10)  # creating node type object with name 'a'
# print(a.value)


# creating Linkedlist 
head=Node(10)   # creating first node as starting pointer of the node
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)

# print the linked list 
temp=head
while temp!=None:
    print(f"{temp.value}-->" , end="")  # end=" " , define to print linkedlist value with one line
    temp=temp.next