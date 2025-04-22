# leetcode 543 二叉树的直径
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1
            l_left = dfs(node.left) + 1
            l_right = dfs(node.right) + 1
            nonlocal ans
            ans = max(ans, l_left + l_right)
            return max(l_left, l_right)
        dfs(root)
        return ans