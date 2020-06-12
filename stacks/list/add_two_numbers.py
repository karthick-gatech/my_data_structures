class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


head1 = ListNode(2)
head1.next = ListNode(4)
head1.next.next = ListNode(3)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(4)


def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    p = l1
    q = l2
    current = dummy_head
    carry = 0
    while p and q:
        x = p.val if p else 0
        y = q.val if q else 0
        sum = carry + x + y
        #print sum
        carry = sum / 10
        current.val = sum % 10
        current.next = ListNode(0)
        current = current.next
        p = p.next if p else None
        q = q.next if q else None
    if carry > 0:
        current.val = carry
    return dummy_head


head3 = addTwoNumbers(head1, head2)
print head3.val, head3.next.val, head3.next.next.val
if head3.next.next.next and head3.next.next.next.val != 0:
    print head3.next.next.next.val

