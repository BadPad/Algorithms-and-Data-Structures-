class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last_node = self.head
        while last_node.Next:
            last_node = last_node.Next
        last_node.Next = newNode

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("please provide valid node as previous node")
            return
        newNode = Node(data)
        newNode.Next = prev_node.Next
        prev_node.Next = newNode

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.Next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.Next

        if cur_node is None:
            return

        prev.Next = cur_node.Next
        cur_node = None

    def delete_node_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.Next
                cur_node = None
                return

            prev = None
            count = 0

            while cur_node and count != pos:
                prev = cur_node
                cur_node = cur_node.Next
                count += 1

            if cur_node is None:
                return
            prev.Next = cur_node.Next
            cur_node = None
    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.Next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1+ self.len_recursive(node.Next)

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return

        prev1 = None
        cur1 = self.head
        while cur1 and cur1.data != key1:
            prev1 = cur1
            cur1 = cur1.Next

        prev2 = None
        cur2 = self.head
        while cur2 and cur2.data != key2:
            prev2 = cur2
            cur2 = cur2.Next

        if not cur1 or not cur2:
            return

        if prev1:
            prev1.Next = cur2
        else:
            self.head = cur2

        if prev2:
            prev2.Next = cur1
        else:
            self.head = cur1

        cur1.Next, cur2.Next = cur2.Next, cur1.Next

    def rev_iteratively(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.Next
            cur.Next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def merge_linkedlist(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.Next
            else:
                s = q
                q = s.Next
            new_Head = s

        while p and q:
            if p.data <= q.data:
                s.Next = p
                s = p
                p = s.Next
            else:
                s.Next = q
                s = q
                q = s.Next

        if not p:
            s.Next = q
        if not q:
            s.Next = p

        return new_Head

    def remove_dupes(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                prev.Next = cur.Next
                cur = None
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = cur.Next

    def nth_to_last(self, n):
        total_len = self.len_iterative()

        cur = self.head

        while cur:
            if total_len == n:
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.Next
        if cur is None:
            return

    def nth_to_last_metho2(self, n):
        p = self.head
        q = self.head

        count = 0

        while q:
            count += 1
            if (count>=n):
                break
            q = q.Next

        if not q:
            print(str(n) + "value is greater than the linked list")
            return

        while p and q.Next:
            p = p.Next
            q = q.Next
        return p.data

    def count_occ(self, data):
        cur = self.head
        count = 0
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.Next
        return count

    def rotate(self, k):
        if self.head and self.head.Next:
            p = self.head
            q = self.head
            prev = None
            count = 0

        while p and count < k:
            prev = p
            p = p.Next
            q = q.Next
            count += 1
        p = prev

        while q:
            prev = q
            q = q.Next
        prev = q

        q.Next = self.head
        self.head = p.Next
        p.Next = None

    def move_tail_to_head(self):
        cur = self.head
        #q = self.head
        prev = None

        while cur.Next:
            prev = cur
            print("inside while", cur.data)
            cur = cur.Next
        cur.Next = self.head
        prev.Next = None
        self.head = cur

    def sum_two_Llist(self, llist):
        p = self.head
        q = llist.head
        sum_llist = LinkedList()
        carry = 0

        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                reminder = s % 10
                sum_llist.append(reminder)
            else:
                carry = 0
                sum_llist.append(s)

            if p:
                p = p.Next
            if q:
                q = q.Next
            if not p or not q and carry > 0:
                sum_llist.append(carry)
        return sum_llist

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.Next


list1 = LinkedList()

list1.append("A")
list1.append("B")
list1.append("C")
list1.append("D")
#list1.insert_after_node(list1.head, 5)
list1.print_list()
list1.delete_node("E")
print("iteratively", list1.len_iterative())
print("recursively", list1.len_recursive(list1.head))
print("swapped Nodes", list1.swap_nodes("D", "C"))
list1.print_list()
print("reversed", list1.rev_iteratively())
list1.print_list()
print("nth to Last ", list1.nth_to_last(4))
print(list1.nth_to_last_metho2(3))

list1.move_tail_to_head()

llist2 = LinkedList()
llist2.append(2)
llist2.append(5)
llist2.append(4)

llist3 = LinkedList()
llist3.append(4)
llist3.append(5)
llist3.append(8)

print("Sum of two Linked List is (254+458)")
s = llist2.sum_two_Llist(llist3)
s.print_list()


