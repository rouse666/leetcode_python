"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
###1递归
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         return self.helper(root.left,root.right)

#     def helper(self,left:TreeNode,right:TreeNode)->bool:
#         if not left and not right:
#             return True
#         if not left or not right:
#             return False
#         if left.val==right.val:
#             return self.helper(left.left,right.right) and self.helper(left.right,right.left)
#         else:
#             return False
###2迭代
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root.left, root.right)]
        while stack:
            pair = stack.pop()
            print(type(pair))
            left = pair[0]
            right = pair[1]
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True
