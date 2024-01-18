class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findSecondMinimumValue(self, root, vals=None):
        """
        :type root: TreeNode
        :rtype: int
        """
        if vals is None:
            vals = []
        if root.val == None:
            return None
        if root.val == root.left.val: 
            return root.val
        if root.val == root.right.val:
            return root.val
        left = self.findSecondMinimumValue(self, root.left, vals)
        right = self.findSecondMinimumValue(self, root.right, vals)
        vals.append(max(left, right))
        return vals[1]

