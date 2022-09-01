# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        maxV = root.val
        self.check(maxV, root)
        return self.ans


    def check(self, maxV, current):
        if current == None:
            return
        if current.val >= maxV:
            self.ans += 1
            maxV = current.val

        self.check(maxV, current.left)
        self.check(maxV, current.right)