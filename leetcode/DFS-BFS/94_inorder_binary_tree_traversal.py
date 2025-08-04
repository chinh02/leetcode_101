# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(data: List[Optional[int]]) -> Optional[TreeNode]:
    if not data or data[0] is None:
        return None

    root = TreeNode(data[0])
    queue = deque([root])
    i = 1

    while queue and i < len(data):
        node = queue.popleft()
        if i < len(data) and data[i] is not None:
            node.left = TreeNode(data[i])
            queue.append(node.left)
        i += 1

        if i < len(data) and data[i] is not None:
            node.right = TreeNode(data[i])
            queue.append(node.right)
        i += 1

    return root

head = [1,None,2,3]
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    def dfs(root, res):
        if root:
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)
    res = []
    dfs(root, res)
    return res

head_list = [1, None, 2, 3]
tree_root = list_to_tree(head_list)
print(inorderTraversal(tree_root))