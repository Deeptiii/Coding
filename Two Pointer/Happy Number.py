# Problem Statement #
# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.


# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false

# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def findSqr(num):
            arr = [int(i) for i in str(num)]
            sums = 0
            for i in range(len(arr)):
                sums+= arr[i]**2
            return sums
        
        fast = n
        slow = n
        
        while True:
            slow = findSqr(slow)
            fast = findSqr(findSqr(fast))
            if fast == slow:
                break
                
        return slow == 1
        