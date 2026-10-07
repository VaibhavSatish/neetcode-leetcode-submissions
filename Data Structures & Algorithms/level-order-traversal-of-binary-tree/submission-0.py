# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        result = []
        if not root:
            return []
        queue.append(root)
        while len(queue) != 0:
            level_size = len(queue)
            temp = []
            for _ in range(level_size):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            result.append(temp)
        return result
            
            
        

        