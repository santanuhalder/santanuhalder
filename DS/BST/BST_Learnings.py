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


class BST:
	def __init__(self):
		self.root = None

	def search(self, value):
		current = self.root
		while current is not None:
			if current.data == value:
				return True
			elif value < current.data:
				current = current.left
			else:
				current = current.right
		return False


if __name__ == "__main__":
	solver = Solution()

	# Example 1
	root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
	# print(solver.maxDepth(root1))  # Expected output: 3

	bst = BST()
	bst.root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
	bst.search(2)







