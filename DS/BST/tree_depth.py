class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def maxDepth(self, root):
		if root is None:
			return 0
		leftDepth = self.maxDepth(root.left)
		rightDepth = self.maxDepth(root.right)

		return max(leftDepth, rightDepth) + 1

	def find_depth(self, root):
		if root is None:
			return 0
		leftDepth = self.maxDepth(root.left)
		rightDepth = self.maxDepth(root.right)

		return max(leftDepth, rightDepth) + 1


if __name__ == "__main__":
	solver = Solution()

	# Example 1
	root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
	# print(solver.maxDepth(root1))  # Expected output: 3

	# Example 2
	root2 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
	# print(solver.maxDepth(root2))  # Expected output: 3

	# Example 3
	root3 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(7, None, TreeNode(9))), TreeNode(3))
	# print(solver.maxDepth(root3))  # Expected output: 4

	t1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
	t2 = TreeNode(1, TreeNode(2, TreeNode(3)))

	t3 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(7, None, TreeNode(9))), TreeNode(3))
	print(solver.find_depth(t3))

	t5 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
	print(solver.find_depth(t5))








