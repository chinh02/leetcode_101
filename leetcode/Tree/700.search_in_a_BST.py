from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == val:
            return root
        
        if root.val > val:   # go left
            return self.searchBST(root.left, val)
        else:                # go right
            return self.searchBST(root.right, val)
        
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Run search
sol = Solution()
result = sol.searchBST(root, 2)

# Print result
if result:
    print("Found node:", result.val)          # Output: 2
    print("Left child:", result.left.val)     # Output: 1
    print("Right child:", result.right.val)   # Output: 3
else:
    print("Value not found in BST")
        