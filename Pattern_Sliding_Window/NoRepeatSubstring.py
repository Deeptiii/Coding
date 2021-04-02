# Problem Statement #
# Given a string, find the length of the longest substring which has no repeating characters.

# Example 1:

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
# Example 3:

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".

# Solved on leetcode, Longest Substring Without Repeating Characters

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    n = len(s)
    winStart = 0
    maxLen = 0
    
    chars=[]
    se =set(chars)
    
    for winEnd in range(n):
        charEnd = s[winEnd]
        chars.append(charEnd)
        se = set(chars)
        
        while len(chars) > len(se):
            charStart = s[winStart]
            chars.pop(0)
            se = set(chars)
            winStart+=1
            
        maxLen= max(maxLen, winEnd -winStart+1)
        
    return maxLen


s = str(input()) 
print(lengthOfLongestSubstring(s))   