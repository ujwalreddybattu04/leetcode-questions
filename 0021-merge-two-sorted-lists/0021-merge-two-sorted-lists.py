class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()  # Dummy node to simplify handling edge cases
        current = dummy  # Pointer to track merged list
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move pointer forward
        
        # Attach remaining elements if any list is not fully traversed
        current.next = list1 if list1 else list2
        
        return dummy.next  # Return merged list (dummy.next skips dummy node)

# Example Usage:
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating example lists: list1 = [1,2,4], list2 = [1,3,4]
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

# Printing merged list
printList(merged_head)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None

        
        