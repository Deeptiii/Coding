# Problem Statement #
# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

# Example 1:

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# Example 2:

# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return n
        
        nonDuplicate = 1
        Next = 1
        
        while Next != n:
            if nums[nonDuplicate-1] != nums[Next]:
                nums[nonDuplicate] = nums[Next]
                nonDuplicate+=1
            Next+=1
            
        return nonDuplicate
            
                
        