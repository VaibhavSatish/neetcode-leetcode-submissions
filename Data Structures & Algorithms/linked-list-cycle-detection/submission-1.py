# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        ptr = head
        while ptr != None:
            if ptr not in seen:
                seen.add(ptr)
            else:
                return True
            ptr = ptr.next
        return False

            
        