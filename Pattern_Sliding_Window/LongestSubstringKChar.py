# Problem Statement #
# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Example 2:

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
# Example 3:

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi". 
 
#User function Template for python3


# Solved on GeeksForGeeks https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1#
class Solution:
    
     def longestKSubstr(self, s, k):
        # code here      
        n = len(s)
        se = len(set(s))

        if se < k:
            return -1
     
        winStart = 0
        maxLen = 0
        
        # res = []
       
        char_frequncy ={}
        
        for winEnd in range(0, n):
            charEnd = s[winEnd]
            if charEnd not in char_frequncy:
                char_frequncy[charEnd] = 0
            char_frequncy[charEnd] +=1
        
            while len(char_frequncy)>k :
                charStart = s[winStart]
                char_frequncy[charStart]-=1
                if char_frequncy[charStart] == 0:
                    del char_frequncy[charStart]
                winStart+=1
            
            maxLen = max(maxLen, winEnd-winStart+1)
        return maxLen


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends