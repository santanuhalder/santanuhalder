def find_min(self, node):
	if node.left is None:
		return node
	return self.find_min(node.left)


def delete_node(self, root, value):
	if root is None:
		return root

	if value < root.data:
		root.left = self.delete_node(root.left, value)
	elif value > root.data:
		root.right = self.delete_node(root.right, value)
	else:
		if root.left is None:
			return root.right
		elif root.right is None:
			return root.left

		temp = self.find_min(root.right)
		root.data = temp.data
		root.right = self.delete_node(root.right, temp.data)

	return root


def delete_method(self, value):
	self.root = self.delete_node(self.root, value)