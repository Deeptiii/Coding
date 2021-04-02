# Words Concatenation (hard) #
# Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

# Example 1:

# Input: String="catfoxcat", Words=["cat", "fox"]
# Output: [0, 3]
# Explanation: The two substring containing both the words are "catfox" & "foxcat".
# Example 2:

# Input: String="catcatfoxfox", Words=["cat", "fox"]
# Output: [3]
# Explanation: The only substring containing both the words is "catfox".

# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        wordsMap = {}
        result = []
        wordCount = len(words)
        
        for i in range(wordCount):            
            if words[i] not in wordsMap:
                wordsMap[words[i]] = 0
            wordsMap[words[i]]+=1
            
        
        wordLen = len(words[0])
        
        for i in range(0, (len(s)- wordCount*wordLen+1)):
            wordSeen = {}
            for j in range(0, wordCount):
                newWordIndex =  i+j*wordLen
                
                word = s[newWordIndex: newWordIndex+wordLen]
                
                if word not in wordsMap:
                    break
                    
                if word not in wordSeen:
                    wordSeen[word] = 0
                wordSeen[word]+=1
                
                if wordSeen[word]>wordsMap[word]:
                    break
                    
                if j + 1 == wordCount:
                    result.append(i)
                    
                
        return result
            
        
        