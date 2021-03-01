# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:


# Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output: [7, 0, 8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
# Output: [8, 9, 9, 9, 0, 0, 0, 1]


# Constraints:

# The number of nodes in each linked list is in the range[1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode(0)
        l1str = ''
        l2str = ''
        while l1 != None:
            l1str = l1str+str(l1.val)
            l1 = l1.next

        while l2 != None:
            l2str = l2str + str(l2.val)
            l2 = l2.next

        carry = 0
        addition = ''
        a = 0
        c = 0
        smallStr = l1str if len(l1str) < len(l2str) else l2str
        largeStr = l2str if len(l1str) < len(l2str) else l1str
        for i in range(len(smallStr)):
            a = int(l1str[i]) + int(l2str[i]) + c
            if c > 0:
                c = 0
            addition = addition + str(int(a % 10))
            c = int(a/10)

        if len(largeStr) != len(smallStr):
            for j in range(i+1, len(largeStr)):
                a = int(largeStr[j]) + c
                if c > 0:
                    c = 0
                addition = addition + str(int(a % 10))
                c = int(a/10)

        if c != 0:
            addition = addition + str(c)

        for z in range(len(str(addition))):

            node = ListNode(int(addition[z]))
            curr.next = node
            curr = curr.next

        return dummy.next
