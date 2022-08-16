class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class linkedlist:
    def __init__(self):
        self.head = None

    def getNode(self, node, M):
        if node is None:
            print("Please provide a valid data")
            return

        while(node is not None):
            last = node
            node = node.next

        while(last is not None):
            last = last.prev
            M -= 1
            if M == 1:
                print(last.data)
                break

    def push(self, new_data):
        newNode = node(new_data)

        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode

        self.head = newNode

    def append(self, new_data):
        newNode = node(new_data)

        newNode.next = None

        if self.head is None:
            self.head = newNode
            self.head.prev = None
            return

        last = self.head
        while(last.next is not None):
            last = last.next

        last.next = newNode

        newNode.prev = last

    def printlist(self, node):
        while (node is not None):
            print(node.data)
            node = node.next



if __name__ == '__main__':

    list1 = linkedlist()

    list1.append(3)

    list1.push(4)

    list1.append(6)

    list1.append(9)

    list1.push(7)

    list1.printlist(list1.head)

    list1.getNode(list1.head, 2)
