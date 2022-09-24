# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            head = None
            return head
        length = 1
        itr = head
        temp = head
        while itr.next:
            length += 1
            itr = itr.next
        count = 1
        while temp:
            if length - n == 0:
                head = head.next
                break
            elif count == length - n :
                temp.next = temp.next.next
                break
            temp = temp.next
            count += 1
        return head