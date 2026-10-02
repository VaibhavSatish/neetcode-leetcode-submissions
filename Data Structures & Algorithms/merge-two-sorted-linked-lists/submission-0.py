# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        cur_node = new_list
        if not list1:
            return list2

        if not list2:
            return list1
        
        while (list1 != None and list2 != None):
            if list1.val < list2.val:
               cur_node.next = list1
               list1 = list1.next
            else:
                cur_node.next = list2
                list2 = list2.next
            cur_node = cur_node.next
        
        cur_node.next = list1 if list1 else list2
        return new_list.next
        

        