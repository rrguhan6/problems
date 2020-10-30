# Given a linked list, determine if it has a cycle in it.
# Follow up:
# Can you solve it without using extra space?


class Node:

    def __init__(self, x):
        self.val = x
        self.next = None


def is_cyclic(head):

    if not head:
        return False

    rabbit = head
    tortoise = head

    while(rabbit.next and rabbit.next.next):
        rabbit = rabbit.next.next
        tortoise = tortoise.next

        if(rabbit == tortoise):
            return True

    return False
