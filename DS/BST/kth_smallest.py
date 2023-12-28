class TreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


class Solution:
	res = list()

	def inOrderTraversal(self, root):
		if not root:
			return
		self.inOrderTraversal(root.left)
		self.res.append(root.data)
		self.inOrderTraversal(root.right)

tree1 = TreeNode(8)
tree1.left = TreeNode(3)
tree1.left.left = TreeNode(1)
tree1.left.right = TreeNode(6)
tree1.left.right.left = TreeNode(4)
tree1.left.right.right = TreeNode(7)
tree1.right = TreeNode(10)
tree1.right.right = TreeNode(14)
tree1.right.right.left = TreeNode(13)


tree2 = TreeNode(5)
tree2.left = TreeNode(2)
tree2.left.left = TreeNode(1)
tree2.right = TreeNode(6)

solution = Solution()
solution.inOrderTraversal(tree2)
x = solution.res

k = 3
print(x[k-1])


