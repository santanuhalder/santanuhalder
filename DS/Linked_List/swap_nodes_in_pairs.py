class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class Solution:
	def swap(self, head):
		dummy = Node(-1)
		previous = dummy
		dummy.next = head

		while head and head.next:
			firsNode = head
			secondNode = head.next

			firsNode.next = secondNode.next
			previous.next = secondNode
			secondNode.next = firsNode
			head = firsNode.next
			previous = firsNode
		return dummy.next

node = Node(10, Node(2, Node(16, Node(7))))
solution = Solution()
headx = solution.swap(node)

while headx:
	print(headx.data, end="--->")
	headx = headx.next
