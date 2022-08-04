class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None

        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head