# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        val = root.val
        while root:
            if abs(target - root.val) < abs(target - val):
                val = root.val
            elif abs(target - root.val) == abs(target - val):
                val = min(val, root.val)
            if root.val < target:
                root = root.right
            else:
                root = root.left

        return val