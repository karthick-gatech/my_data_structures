# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next.next = ListNode(3)
head1.next.next.next.next = ListNode(4)
head1.next.next.next.next.next = ListNode(5)
n = 2

# two pass algorithm.
# We notice that the problem could be simply reduced to another one
# Remove the (L-n+1) th node from the beginning
# where L is the list length. This problem is easy to solve once we found list length LL.

