class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Solution:
	def remove_nodes(self, head, key):
		itr = head

		while itr:
			if itr.next.data == key:
				itr.next = itr.next.next
			itr = itr.next
		return head

	def remove_nodes_recur(self, head, key):
		if not head.next:
			return None
		if head.data == key:
			head.next = head.next.next
		else:
			head = head.next
		return self.remove_nodes_recur(head, key)


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(2)
node.next.next.next.next = Node(4)

sol = Solution()
# head = sol.remove_nodes(node, 4)
#
# while head:
# 	print(head.data)
# 	head = head.next

head1 = sol.remove_nodes_recur(node, 4)
while head1:
	print(head1.data)
	head1 = head1.next

