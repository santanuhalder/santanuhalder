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



ls = LinkedList()
ls.insert_at_beginning('santanu')
ls.insert_at_beginning('praveen')
ls.insert_at_beginning('vish')
ls.insert_values(["valencia", "culver city"])
ls.print_ls()
print(ls.get_length())
# ls.insert_at("hello", 0)
ls.insert_at("madam", 2)
ls.print_ls()
        



