# leetcode 104 二叉树的最大深度
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    

"""
时间复杂度：O(n)
空间复杂度：O(n)
"""