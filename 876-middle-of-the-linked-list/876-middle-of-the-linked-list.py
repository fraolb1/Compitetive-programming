# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        itr = head
        length = 1
        count = 0
        while temp.next:
            temp = temp.next
            length += 1

        if length%2 == 0:
            while itr.next:
                if count == length/2:
                    return itr
                itr = itr.next
                count += 1
            return itr
        else:
            while itr.next:
                if count == length//2:
                    return itr
                itr = itr.next
                count += 1
            return itr