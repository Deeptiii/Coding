# Permutation in a String (hard) #
# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters it will have n!n! permutations.

# Example 1:

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.
# Example 3:

# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
# Example 4:

# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.

# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        winStart =0
        n = len(s2)
        k = len(s1)
        sub = {}
        matched = 0
        
        for i in range(k):
            if s1[i] not in sub:
                sub[s1[i]] = 0
            sub[s1[i]]+=1
            
        for winEnd in range(n):
            charEnd = s2[winEnd]
            
            if charEnd in sub:
                sub[charEnd]-=1
                if sub[charEnd] == 0: # all occurences should match
                    matched+=1

            if matched == len(sub): 
                return True
            
            if winEnd >= k-1:
                charStart = s2[winStart]
                winStart+=1
                if charStart in sub:
                    
                    if sub[charStart] == 0:
                        matched-=1
                    sub[charStart]+=1
                    
        return False
        
#         winStart =0
#         n = len(s2)
#         k = len(s1)
#         s1Arr = list(s1)
#         s1Arr.sort()
        
#         winArr = []
#         temp = []
#         for winEnd in range(n):   
#             charEnd = s2[winEnd]
#             winArr.append(charEnd)            
            
#             if len(winArr) > k:
#                 winArr.pop(0)
#                 winStart+=1
                
#             if k == len(winArr):
#                 temp = sorted(winArr)
#                 if(temp == s1Arr):
#                     return True
            
#         return False

    
            