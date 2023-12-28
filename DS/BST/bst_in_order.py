class TreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

class Solution:
	def __init__(self):
		self.result = []
	# def inorderTraversal(self, root):
	# 	self.inorder(root)

	def inorder(self, node):
		if node is None:
			return
		self.inorder(node.left)
		self.result.append(node.data)
		self.inorder(node.right)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(10)

inorderTraversal = Solution()
# inorderTraversal.inorderTraversal(root)

inorderTraversal.inorder(root)
result = inorderTraversal.result

print("Inorder Traversal:", result)


