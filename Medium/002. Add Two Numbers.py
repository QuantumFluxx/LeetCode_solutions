class Solution(object):
    def addTwoNumbers(self, L1, L2):
        dummyHead = ListNode(None)
        tail = dummyHead

        addOne = 0
        while L1 or L2 or addOne:
            newVal = (L1.val if L1 else 0) + (L2.val if L2 else 0) + addOne
            addOne, newVal = divmod(newVal, 10)

            tail.next = ListNode(newVal)
            tail = tail.next

            if L1: L1 = L1.next
            if L2: L2 = L2.next

        return dummyHead.next