# String Anagrams (hard) #
# Given a string and a pattern, find all anagrams of the pattern in the given string.

# Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

# abc
# acb
# bac
# bca
# cab
# cba
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

# Example 1:

# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
# Example 2:

# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        winStart = 0
        n = len(s)
        k = len(p)
        matched = 0
        sub = {}
        res = []
        
        for i in range(k):
            if p[i] not in sub:
                sub[p[i]] = 0
            sub[p[i]]+=1
            
        for winEnd in range(n):
            charEnd = s[winEnd]
            
            if charEnd in sub:
                sub[charEnd]-=1
                if sub[charEnd] == 0:
                    matched+=1
            
            
            if matched == len(sub):
                res.append(winStart)
                
            if winEnd >= k-1:
                charStart = s[winStart]
                winStart+=1
                
                if charStart in sub:
                    if sub[charStart] == 0:
                        matched-=1
                    sub[charStart]+=1
                
        return res
    
    
#          winStart = 0
#             n = len(s)
#             k = len(p)
#             ana = []
#             ans = []
#             p = sorted(p)
#             for winEnd in range(n):
#                 charEnd = s[winEnd]
#                 ana.append(charEnd)

#                 if len(ana)>k:
#                     ana.pop(0)
#                     winStart+=1

#                 if k == len(ana) and sorted(ana) == p:
#                     ans.append(winStart)

#             return ans