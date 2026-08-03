# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # [optional prefix: ... -> prefix_tail] -> [segment: segment_head -> ... -> segment_tail] -> [optional suffix: suffix_head -> ...]
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        if (
            not head.next or left >= right
            # or left > list length  # Guaranteed by problem.
        ):
            return head

        # Move to the first node of the segment being reversed.
        n = 1
        current = head  # points to the node at position n
        prefix_tail = None

        while n < left and current:
            prefix_tail = current
            current = current.next
            n += 1

        # `left` is within the list because `1 <= left <= right <= list length`, so `current` is not `None`.
        assert current is not None

        # The first node of the segment becomes its tail after reversal.
        segment_tail = current
        segment_head = None

        # Reverse the nodes from left through right.
        while n <= right and current:
            next_node = current.next

            current.next = segment_head

            segment_head = current
            current = next_node
            n += 1

        # Connect the reversed segment to the remaining suffix.
        suffix_head = current
        segment_tail.next = suffix_head

        # Connect the preceding prefix to the reversed segment.
        if prefix_tail:
            prefix_tail.next = segment_head
            return head

        # The reversed segment starts at the original head.
        return segment_head


def display(head: Optional[ListNode]) -> None:
    if not head:
        return

    if not head.next:
        print(head.val)
        return

    print(head.val, end=" ")
    display(head.next)
