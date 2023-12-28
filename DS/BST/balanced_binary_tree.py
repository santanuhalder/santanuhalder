class TreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


class Solution:
	def isBalanced(self, root):
		if root is None:
			return 0
		leftDepth = self.isBalanced(root.left)
		rightDepth = self.isBalanced(root.right)

		if abs(leftDepth-rightDepth) > 1:
			return -1
		return max(leftDepth, rightDepth) + 1


t1 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), None),
				TreeNode(2, None, TreeNode(3, TreeNode(4), TreeNode(4))))

solver = Solution()
print(solver.isBalanced(t1))

t2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), None), None), TreeNode(5))
s = solver.isBalanced(t2)
if s == -1:
	print("The tree is unbalanced")

