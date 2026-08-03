# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next or left == right:
            return head

        n = 1
        before = None
        curr = head

        while n < left and curr:
            before = curr
            curr = curr.next
            n += 1

        tail = curr
        prev = None

        while n <= right and curr:
            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node
            n += 1

        tail.next = curr

        if before:
            before.next = prev
            return head

        return prev


def display(head: Optional[ListNode]) -> None:
    if not head:
        return

    if not head.next:
        print(head.val)
        return

    print(head.val, end=" ")
    display(head.next)
