from heapq import heappush, heappop
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    # To compare ListNode objects in heapq
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # Push the first node of each list into the heap
        for idx, l in enumerate(lists):
            if l:
                heappush(min_heap, (l.val, idx, l))  # (value, index, node)
        
        dummy = ListNode()  # Dummy node to start the merged list
        curr = dummy
        
        while min_heap:
            val, idx, node = heappop(min_heap)  # Get the smallest node
            curr.next = node  # Append to merged list
            curr = curr.next
            
            if node.next:  # If there are more nodes in this list, push next node
                heappush(min_heap, (node.next.val, idx, node.next))
        
        return dummy.next  # Return merged list starting from the first node

# Example Usage:
# Convert input list format to ListNode and test accordingly.
