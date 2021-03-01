# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1 -> 2
# Output: false
# Example 2:

# Input: 1 -> 2 -> 2 -> 1
# Output: true

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        li = []

        node = head
        if node == None:
            return True

        end = head
        length = 0
        skipMiddle = True

        while end != None:
            length += 1
            end = end.next

        if length % 2 == 0:
            skipMiddle = False

        half = int(length/2)
        i = 1
        while i <= half:
            li.append(node.val)
            node = node.next
            i += 1

        if skipMiddle:
            node = node.next
            i += 1

        while node != None and len(li) > 0:
            if li[len(li)-1] == node.val:
                li.pop()
                node = node.next
            else:
                return False

        return True
