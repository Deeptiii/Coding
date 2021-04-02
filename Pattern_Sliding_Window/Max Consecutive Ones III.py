# Problem Statement #
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

# Example 1:

# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
# Example 2:

# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

# Leetcode https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        winStart = 0
        frequency = {}
        maxRepeatingOne =0 
        maxLen = 0
        
        for winEnd in range(n):
            charEnd = A[winEnd]
            if charEnd not in frequency:
                frequency[charEnd] = 0
            frequency[charEnd]+=1
            if(charEnd == 1):
                maxRepeatingOne = max(maxRepeatingOne, frequency[charEnd])
            
            if winEnd - winStart +1 - maxRepeatingOne > K:
                charStart = A[winStart]
                frequency[charStart]-=1
                if frequency[charStart] == 0:
                    del frequency[charStart]
                    
                winStart+=1
                
            maxLen = max(maxLen, winEnd-winStart+1)
        return maxLen