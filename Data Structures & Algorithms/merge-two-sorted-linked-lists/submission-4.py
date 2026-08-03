# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Dummy node before the merged list.
        dummy = ListNode()

        # Heads of the remaining unmerged lists.
        l1, l2 = list1, list2

        # Tail of the merged list.
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        # Connect the remaining non-empty list.
        tail.next = l1 if l1 else l2

        return dummy.next


def display(head: Optional[ListNode]) -> None:
    while head:
        print(head.val, end=" ")
        head = head.next

    print()
