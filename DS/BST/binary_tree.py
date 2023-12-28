class TreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def add_a_child(self, val):
		if val == self.data:
			return
		if val < self.data:
			if self.left:
				self.left.add_a_child(val)
			else:
				self.left = TreeNode(val)
		if val > self.data:
			if self.right:
				self.right.add_a_child(val)
			else:
				self.right = TreeNode(val)

	def in_order_traversal(self):
		elements = list()
		# add left tree
		if self.left:
			elements += self.left.in_order_traversal()
		# add self.data
		elements.append(self.data)
		# add right tree
		if self.right:
			elements += self.right.in_order_traversal()
		return elements


	def search(self, val):
		if self.data == val:
			return True

		if val < self.data:
			if self.left:
				return self.left.search(val)
			else:
				return False

		if val > self.data:
			if self.right:
				return self.right.search(val)
			else:
				return False

	def find_min(self):
		if self.left:
			return self.left.find_min()
		else:
			return self.data

	def find_max(self):
		if self.right:
			return self.right.find_max()
		else:
			return self.data

	def calc_sum(self):
		left_sum = self.left.calc_sum() if self.left else 0
		right_sum = self.right.calc_sum() if self.right else 0
		return self.data + left_sum + right_sum

	def max_depth(self):
		max = 0
		if self.left:
			max += 1
def build_a_tree(nums):
	bTree = TreeNode(nums[0])
	for i in range(1, len(nums)):
		bTree.add_a_child(nums[i])
	return bTree

numb = [1, 2, 3, 4, 5]
tree = build_a_tree(numb)
# print(tree.in_order_traversal())
# print(tree.find_min())
# print(tree.find_max())
print(tree.calc_sum())

# countries = ["USA", "China", "USA", "India", "Germany", "France", "India", "France"]
# countryTree = build_a_tree(countries)
# print(countryTree.in_order_traversal())
#
# # # print(tree.search(34))
# # print(countryTree.search("Brazil"))
# print(countryTree.find_min())
# print(countryTree.find_max())