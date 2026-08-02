# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverseTree(node, p, q):
            # if p or q is node: return node
            if p.val == node.val or q.val == node.val:
                return node
            # elif both < node: investigate left child
            elif p.val < node.val and q.val < node.val:
                return traverseTree(node.left, p, q)
            # elif both > node: investiagte right child
            elif p.val > node.val and q.val > node.val:
                return traversetree(node.right, p, q)
            # else one < node, one > node: return node
            else:
                return node

        return traverseTree(root, p, q)

            