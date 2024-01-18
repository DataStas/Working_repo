class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def searchBST(root: TreeNode, val):
#     """
#     :type root: TreeNode
#     :type val: int
#     :rtype: TreeNode
#     """
#     if not root or not root.left or root.right:
#         return None
#     if root.val == val:
#         return [root.val, root.left.val, root.right.val]
#     searchBST(root.left, val)
#     searchBST(root.right, val)
#     return []

def searchBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    stack, subtree = [], None
    while True:
        while root:
            if root.val == val: subtree = root
            stack.append(root)
            root = root.left
        if subtree: return subtree
        if not stack: return None
        root = stack.pop().right


# class Solution(object):
#     def searchBST(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode
#         """
#         if not root:
#             return None
#         if root.val == val:
#             return root
#         l = self.searchBST(root.left, val)
#         r = self.searchBST(root.right, val)
#         if l:
#             return l
#         elif r:
#             return r
#         else:
#             return None