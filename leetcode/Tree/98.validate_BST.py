from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val):
            if node is None: return True
            if node.val < min_val or node.val > max_val: return False            
            return dfs(node.left, min_val, node.val - 1) and dfs(node.right, node.val+1, max_val)
        return dfs(root, float("-inf"), float("inf"))
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

sol = Solution()
result = sol.isValidBST(root)
print(result)

