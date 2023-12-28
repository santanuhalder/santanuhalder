class TreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


class Solution:
	res = []

	def range_sum(self, node, l, r):
		if not node:
			return 0
		if node.data > r:
			return self.range_sum(node.left, l, r)
		if node.data < l:
			return self.range_sum(node.right, l, r)
		return node.data + self.range_sum(node.left, l, r) + self.range_sum(node.right, l, r)

	def inorder(self, node):
		if not node:
			return
		self.inorder(node.left)
		self.res.append(node.data)
		self.inorder(node.right)


tree1 = TreeNode(10)
tree1.left = TreeNode(5)
tree1.left.left = TreeNode(3)
tree1.left.right = TreeNode(7)
tree1.right = TreeNode(15)
tree1.right.right = TreeNode(18)

solution = Solution()
solution.inorder(tree1)
r = solution.res
print(r)
l = 7
r = 15
print(solution.range_sum(tree1, l, r))

