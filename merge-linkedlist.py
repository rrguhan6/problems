# Merge two sorted linked lists and return it as a new list. The new list should
# be made by splicing together the nodes of the first two lists.
# For example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


def merger(l1, l2):

    ret = l3 = Node(0)

    while(l1 and l2):

        if(l1.data < l2.data):
            l3.next = l1
            l1 = l1.next
        else:
            l3.next = l2
            l3 = l3.next

        l3 = l3.next

    l3.next = l1 or l2  # remaining lists

    return ret.next
