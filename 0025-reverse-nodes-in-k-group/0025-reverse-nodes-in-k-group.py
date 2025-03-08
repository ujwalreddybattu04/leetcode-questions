class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Count total nodes
        def count_nodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        total_nodes = count_nodes(head)
        if k <= 1 or not head or total_nodes < k:
            return head  # No need to reverse

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while total_nodes >= k:
            # Reverse k nodes
            prev, curr = None, prev_group_end.next
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # Connect reversed part to the rest of the list
            temp = prev_group_end.next  # Old head becomes the new tail
            prev_group_end.next = prev  # New head after reversal
            temp.next = curr  # Connect to remaining nodes
            prev_group_end = temp  # Move group end forward
            
            total_nodes -= k
        
        return dummy.next

        