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

        display(head)

        # display(self.reverse(head, 4))

        n = 1
        prev = None
        curr = head

        while n < left and curr:
            n += 1
            next = curr.next

            prev = curr
            curr = next

        print(prev.val)
        prev.next = self.reverse(curr, right - n)

        display(head)

        return head

    def reverse(self, head: Optional[ListNode], right: int) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        n = 0
        prev = None
        curr = head

        while n <= right and curr:
            n += 1
            next = curr.next

            curr.next = prev

            prev = curr
            curr = next

        head.next = curr

        return prev

def display(head: Optional[ListNode]) -> None:
    if not head:
        return

    if not head.next:
        print(head.val)
        return

    print(head.val, end=" ")
    display(head.next)
