class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Count nodes
        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        # Dummy handles removing the head
        dummy = ListNode(0, head)

        curr = dummy

        # Move to node BEFORE the node we want to delete
        for _ in range(count - n):
            curr = curr.next

        # Skip the node
        curr.next = curr.next.next

        return dummy.next