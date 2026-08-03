# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next or left >= right:
            return head

        # Move to the first node of the segment being reversed.
        n = 1
        current = head
        prefix_tail = None

        while n < left and current:
            prefix_tail = current
            current = current.next
            n += 1

        # The first node of the segment becomes its tail after reversal.
        segment_tail = current
        reversed_head = None

        # Reverse the nodes from left through right.
        while n <= right and current:
            next_node = current.next

            current.next = reversed_head

            reversed_head = current
            current = next_node
            n += 1

        # Connect the reversed segment to the remaining suffix.
        assert segment_tail is not None
        segment_tail.next = current

        # Connect the preceding prefix to the reversed segment.
        if prefix_tail:
            prefix_tail.next = reversed_head
            return head

        # The reversed segment starts at the original head.
        return reversed_head


def display(head: Optional[ListNode]) -> None:
    if not head:
        return

    if not head.next:
        print(head.val)
        return

    print(head.val, end=" ")
    display(head.next)
