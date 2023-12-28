# Code: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list.py
# Exercise: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list_exercise.md
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self, data):
        node = Node(data, None)
        node.next = self.head
        self.head = node

    def insert_at_the_end(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node


    def print_list(self):
        itr = self.head
        txt = ""
        while itr:
            spaces = ""
            if itr.next is not None:
                spaces = " --> "
            txt += str(itr.data) + spaces
            itr = itr.next
        print(txt)

    def insert_values(self, values):
        for data in values:
            self.insert_at_the_end(data)

    def get_ls_length(self):
        itr = self.head
        level = 0
        while itr:
            itr = itr.next
            level += 1
        return level

    def remove_at(self, index):
        if index < 0 or index >= self.get_ls_length():
            raise Exception("Not a valid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


    def insert_at(self, index, data):
        if index < 0 or index > self.get_ls_length():
            raise Exception("Invalid index")
        node = Node(data, None)
        if index == 0:
            self.insert_at_the_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node.next = itr.next
                itr.next = node
            itr = itr.next
            count += 1


        counter = 0
        itr = self.head
        while counter < index:
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
        return prev

    def remove_dup(self):
        itr = self.head
        count = 0
        while itr and itr.next:
            count += 1
            if itr.data == itr.next.data:
                itr.next = itr.next.next
            else:
                itr = itr.next
        return self.head

    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    def print_by_head(self, head):
        itr = head
        txt = ""
        while itr:
            txt += str(itr.data) + "--->"
            itr = itr.next
        print(txt)


    def merge_lists(self, head1, head2):
        curr1, curr2 = head1, head2
        new_ls = LinkedList()
        new_ls.head = None

        while curr1 and curr2:
            data1 = curr1.data
            data2 = curr2.data
            if data1 < data2:
                new_ls.insert_at_the_end(data1)
                curr1 = curr1.next
            else:
                new_ls.insert_at_the_end(data2)
                curr2 = curr2.next
        while curr1:
            new_ls.insert_at_the_end(data1)
            curr1 = curr1.next
        while curr2:
            new_ls.insert_at_the_end(data2)
            curr2 = curr2.next
        return new_ls.head







ls1 = LinkedList()
# ls.insert_values(['valencia', 'stevenson ranch', 'eastvale', 'culver city', 'santa monica'])
# ls.insert_values([3, 3, 3])
ls1.insert_values([1, 3, 5])
h1 = ls1.head

ls2 = LinkedList()
ls2.insert_values([2, 4, 6])
h2 = ls2.head



# h1 = ls.remove_dup()
# ls.print_by_head(h1)






