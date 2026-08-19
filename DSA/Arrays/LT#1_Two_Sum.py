'''LeetCode #1 — Two Sum

You've actually already looked at this problem before, so this is a good one to solve yourself first.

Problem

Given an integer array nums and an integer target, return the indices of the two numbers such that they add up to target.

Example:

nums = [2, 7, 11, 15]
target = 9

Expected:

[0, 1]'''

----------------------------------------------------------------------------------------------------------------
# LeetCode #1 - Two Sum
# Pattern: Hash Map / Dictionary
#
# Goal:
# Find two numbers in the array whose sum equals the target
# and return their indexes.
#
# Example:
# nums = [2, 7, 11, 15]
# target = 9
# Answer = [0, 1]
#
# Key idea:
# For every number, calculate its complement:
# complement = target - current_number
#
# Then check whether the complement was already seen.
# If yes, we found the two numbers.
# If no, store the current number and its index.

class Solution:
    def twoSum(self, nums, target):
        # Dictionary to store:
        # number -> index
        seen = {}

        # enumerate() gives both index and value
        for i, num in enumerate(nums):

            # Find the number required to reach the target
            complement = target - num

            # Check if the required number was already seen
            if complement in seen:
                return [seen[complement], i]

            # Store current number and its index
            seen[num] = i

        # Return empty list if no pair is found
        return []


# Local testing
solution = Solution()

nums = [2, 7, 11, 15]
target = 9

print(solution.twoSum(nums, target))
# Output: [0, 1]


# Time Complexity: O(n)
# Space Complexity: O(n)
