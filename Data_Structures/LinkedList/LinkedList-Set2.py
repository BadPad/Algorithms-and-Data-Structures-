class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self, pre_node, new_data):
        if pre_node is None:
            print("Previous node must be present in Linked List")
            return

        newNode = Node(new_data)

        newNode.next = pre_node.next

        pre_node.next = newNode

    def append(self, new_data):

        newNode = Node(new_data)

        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = newNode

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    list1 = linkedlist()

    list1.append(4)

    list1.push(8)

    list1.append(9)

    list1.append(2)

    list1.insertAfter(list1.head, 5)

    print(list1.head.data)

    print("linked list created is: ")

    list1.printList()
