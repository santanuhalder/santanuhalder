class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, None)
        node.next = self.head
        self.head = node


    def reverse_the_list(self):
        prev, curr = None, self.head


    def print_ls(self):
        itr = self.head
        ls_str = " "
        while itr:
            ls_str += itr.data + "-->"
            itr = itr.next
        print(ls_str)

    def insert_at_the_end(self, data):
        node = Node(data, None)
        if self.head is None:
            node.next = self.head
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node

    def insert_values(self, values):
        for val in values:
            self.insert_at_the_end(val)

    def get_length(self):
        len = 0
        itr = self.head
        while itr:
            len += 1
            itr = itr.next
        return len

    def insert_at(self, data, index):
        if self.head is None or index < 0 or index > self.get_length():
            raise Exception("In valid index entered")

        node = Node(data, None)
        if index == 0:
            self.insert_at_beginning(data)

        counter = 0
        itr = self.head
        while counter < index - 1:
            itr = itr.next
            counter += 1
        node.next = itr.next
        itr.next = node


    def reverse_list(self):
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt



ls = LinkedList()
ls.insert_values(["valencia", "culver city", "stevenson ranch", "santa clarita"])
ls.print_ls()
ls.reverse_list()

ls.print_ls()




