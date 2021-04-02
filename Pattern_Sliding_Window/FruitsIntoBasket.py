# Problem Statement #
# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# Example 1:

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
# Example 2:

# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']


# Solved on Leetcode https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        frequency ={}
        n = len(tree)
        winStart =0
        maxLen = 0
        
        for winEnd in range(n):
            numEnd = tree[winEnd]
            if numEnd not in frequency:
                frequency[numEnd] = 0
            frequency[numEnd]+=1
            
            print(frequency)
            
            while len(frequency) >2:
                numStart = tree[winStart]
                frequency[numStart]-=1
                if frequency[numStart] == 0:
                    del frequency[numStart]
                winStart+=1
                   
            maxLen = max(maxLen, winEnd-winStart +1)
            
        return maxLen