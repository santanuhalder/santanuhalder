class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def __init__(self):
		# List to hold the values in order.
		self.nodes = []

	def inorderTraversal(self, node):
		if not node:
			return

		self.inorderTraversal(node.left)
		self.nodes.append(node.val)
		self.inorderTraversal(node.right)






solution = Solution()
tree1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
solution.inorderTraversal(tree1)

res = solution.nodes
# min_diff = float('inf')
# for i in range(1, len(res)):
# 	min_diff = min(min_diff, res[i] - res[i-1])

print(res)


