class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print(self):
        if self.head is None:
            print("The LinkedList is empty")
        else:
            itr = self.head
            ls_string = ""
            while itr:
                ls_string += str(itr.data) + "--->"
                itr = itr.next
            print(ls_string)

    def get_length(self):
        length = 0
        itr = self.head
        if itr is None:
            return length
        else:
            while itr:
                length += 1
                itr = itr.next
        return length

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.insert_at_beginning(data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node

    def insert_values(self, values):
        self.head = None
        for val in values:
            self.insert_at_end(val)

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        counter = 0
        itr = self.head
        while counter < index - 1:
            itr = itr.next
            counter += 1
        itr.next = itr.next.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        counter = 0
        itr = self.head
        while counter < index - 1:
            itr = itr.next
            counter += 1
        node = Node(data, None)
        node.next = itr.next
        itr.next = node






ls = LinkedList()
# ls.insert_at_beginning(90)
# ls.insert_at_beginning(10)
# ls.insert_at_beginning(15)
# ls.insert_at_end(100)
# ls.insert_at_end(10)
list_values = [12, 10, 45, 5]
ls.insert_values(list_values)
ls.print()
ls.insert_at(1, 23)
ls.print()








