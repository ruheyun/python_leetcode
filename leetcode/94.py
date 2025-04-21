# leetcode 94 二叉树的遍历
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root):
            if root is None: return
            dfs(root.left)
            nonlocal ans
            ans.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return ans

"""
时间复杂度：O(n)
空间复杂度：O(n)
"""
        