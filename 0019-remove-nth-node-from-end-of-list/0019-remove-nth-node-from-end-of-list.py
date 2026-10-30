# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        if head is None:
            return None

        ptr = head
        num = 0

        while ptr is not None:
            ptr = ptr.next
            num += 1

        steps = num - n

        if steps == 0:
            return head.next

        tmp = head
        ptr = None

        for i in range(steps):
            ptr = tmp
            tmp = tmp.next

        ptr.next = tmp.next

        return head


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

solution = Solution().removeNthFromEnd(l, 1)

ptr = solution

while ptr is not None:
    print(ptr.val)
    ptr = ptr.next