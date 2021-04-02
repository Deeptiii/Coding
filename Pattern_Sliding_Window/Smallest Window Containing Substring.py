# Smallest Window containing Substring (hard) #
# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

# Example 1:

# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"
# Example 2:

# Input: String="abdabca", Pattern="abc"
# Output: "abc"
# Explanation: The smallest substring having all characters of the pattern is "abc".
# Example 3:

# Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.

# https://leetcode.com/problems/minimum-window-substring/ 


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        winStart = 0
        n = len(s)
        k = len(t)
        sub = {}
        matched = 0
        minlen = n+1
        subStrStart = 0
        
        # Get the frequency of all characters from the pattern
        for i in range(k): 
            if t[i] not in sub:
                sub[t[i]] = 0
            sub[t[i]]+=1
            
        
        for winEnd in range(n):
            charEnd = s[winEnd]
            
            if charEnd in sub:
                sub[charEnd] -=1
                # Every time a charcter is matched count it in

                if sub[charEnd] >=0:
                    matched+=1
                    
                    
            while matched == k: # Start shrinking window wwn all characters are matched
                if minlen > winEnd -winStart +1:
                    minlen = winEnd -winStart +1
                    subStrStart = winStart                
                
                charStart = s[winStart]
                winStart+=1
                if charStart in sub:
                    if sub[charStart] == 0:
                        matched -=1
                    sub[charStart]+=1
        
        return "" if minlen > n else s[subStrStart: subStrStart + minlen]
                    
                