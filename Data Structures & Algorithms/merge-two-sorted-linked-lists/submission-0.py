# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        p1, p2 = None, None
        l1, l2 = list1, list2
        head = l1 if l1.val <= l2.val else l2

        while l1 and l2:
            print(l1.val, l2.val)

            if l1.val < l2.val:
                temp = l1.next
                l1.next = l2
                p1 = l1
                l1 = temp

            elif l1.val > l2.val:
                temp = l2.next
                l2.next = l1
                p2 = l2
                l2 = temp

            else:
                # Choose list 1 node if tie.
                temp = l1.next
                l1.next = l2
                p1 = l1
                l1 = temp

            display(head)
            print()

        return head


def display(head: Optional[ListNode]) -> None:
    while head:
        print(head.val, end=" ")
        head = head.next

    print()
