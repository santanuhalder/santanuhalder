class DLNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def is_palindrome(self, head):
        tail = head
        while tail.next:
            tail = tail.next
        start = head
        end = tail

        while start != end:
            if start.data != end.data:
                return False
            start = start.next
            end = end.prev

        return True


dl1 = DLNode(1)
dl2 = DLNode(10)
dl1.next = dl2
dl2.prev = dl1
dl3 = DLNode(7)
dl2.next = dl3
dl3.prev = dl2

solution = Solution()
solution.is_palindrome(dl1)

head1 = DLNode("a")
head1.next = DLNode("b")
head1.next.prev = head1
head1.next.next = DLNode("x")
head1.next.next.prev = head1.next
x = solution.is_palindrome(head1)
print(x)
