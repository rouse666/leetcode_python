"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         res=[]
#         cur_level=[root] if root else []

#         while cur_level:
#             cur_val=[]
#             next_level=[]
#             for node in cur_level:
#                 cur_val.append(node.val)
#                 if node.left:
#                     next_level.append(node.left)
#                 if node.right:
#                     next_level.append(node.right)

#             res.append(cur_val)
#             cur_level=next_level
#         return res
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
                r = queue.pop(0)
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            res.append(tmp)
        return res

