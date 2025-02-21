# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current is not None: 
            # we make nextNode = 2 and store this
            nextNode = current.next
            # we make 2, the next node, equal to prev, which was none
            current.next = prev
            # then we make prev, which set the next node equal to None, equal to the curr val, 1
            prev = current
            # then we make 1 become the Next node, 2 and we repeat
            current = nextNode
        # once we have traversed the whole list, we make the head, which if it was 5 numbers 1-5, become prev which is 5. now the full list has been reversed
        head = prev
        return head
            