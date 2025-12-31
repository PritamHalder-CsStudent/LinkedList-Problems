# check a linkedlist is palindrom or not 

# Logic:
# Reverse the second half of the linked list
# Compare both halves node by node



class Solution:
    def reverseLL(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        

    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        # 1. Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        second_half = self.reverseLL(slow)

        # 3. Compare both halves
        first_half = head
        temp = second_half

        while temp:
            if first_half.data != temp.data:
                return False
            first_half = first_half.next
            temp = temp.next

        return True   