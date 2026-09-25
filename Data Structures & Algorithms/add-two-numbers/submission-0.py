class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:

            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return dummy.next