class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Solution:
    def merge_list(self):
        pass

    def printList(self, head):
        itr = head
        while itr:
            print(itr.data, end=" ")
            itr = itr.next
        print()


    def merge_lists(self, l1, l2):
        new_ls = Node(None, None)
        current = new_ls

        while l1 and l2:
            if l1.data < l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2

        return new_ls.next



if __name__ == "__main__":
    solution = Solution()

    ls1 = Node(1, Node(3,  Node(5, Node(9))))
    solution.printList(ls1)

    ls2 = Node(2, Node(8))
    solution.printList(ls2)

    head = solution.merge_lists(ls1, ls2)
    solution.printList(head)

