class Node:
  def __init__(self, value=0, next=None):
    self.value = value
    self.next = next

def printList(l):
    value = []
    while(l):
        value.append(l.value)
        l = l.next
    print(' -> '.join(map(str, value)))

def linked_list_sum_iterative(list1, list2):
  res = Node()
  p1 = list1
  p2 = list2
  curr = res
  carry = 0
  while p1 is not None or p2 is not None or carry != 0:
    sum = carry
    if p1:
      sum += p1.value
      p1 = p1.next
    if p2:
      sum += p2.value
      p2 = p2.next
    curr.value = sum % 10
    carry = sum // 10
    if p1 is not None or p2 is not None or carry != 0:
      curr.next = Node()
      curr = curr.next
  return res

#789
l1 = Node(9, Node(8, Node(7)))
#4789
l2 = Node(9, Node(8, Node(7, Node(4))))
l3 = linked_list_sum_iterative(l1, l2)
printList(l3)
