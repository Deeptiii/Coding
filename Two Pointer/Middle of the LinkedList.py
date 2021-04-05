# Problem Statement #
# Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

# If the total number of nodes in the LinkedList is even, return the second middle node.

# Example 1:

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3
# Example 2:

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Output: 4
# Example 3:

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
# Output: 4

# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        
        while fast!= None and fast.next!= None:
            slow = slow.next
            fast = fast.next.next
            
        return slow