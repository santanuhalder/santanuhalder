class TreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right= right

class Solution:
	def __init__(self):
		self.result = []

	def in_order(self, node):
		if not node:
			return
		self.in_order(node.left)
		self.result.append(node.data)
		self.in_order(node.right)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(10)

inorderTraversal = Solution()
# inorderTraversal.inorderTraversal(root)

inorderTraversal.in_order(root)
result = inorderTraversal.result

print("Inorder Traversal:", result)