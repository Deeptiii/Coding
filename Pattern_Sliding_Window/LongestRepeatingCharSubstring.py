# Problem Statement #
# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:

# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

# Solved on Leetcode

# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        winStart = 0
        frequency = {}
        chars = []
        maxRepeatingChar = 0
        
        maxLength = 0
        
        for winEnd in range(n):
            charEnd = s[winEnd]
            if charEnd not in frequency:
                frequency[charEnd] =0
            frequency[charEnd]+=1
            maxRepeatingChar = max(maxRepeatingChar, frequency[charEnd])
            
            if(winEnd - winStart+1-maxRepeatingChar> k): # when number of other chars excluding maxrepeating char are greated than k start shrinking window
                charStart = s[winStart]
                frequency[charStart] -=1
                if frequency[charStart] == 0:
                    del frequency[charStart]
                winStart+=1
                
            maxLength = max(maxLength, winEnd-winStart+1)
            
        return maxLength
            
            
        