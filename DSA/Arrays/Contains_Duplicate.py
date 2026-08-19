# LeetCode #217 - Contains Duplicate
# Pattern: Hash Set
#
# ---------------------------------------------------------
# Problem:
# ---------------------------------------------------------
# Given an integer array nums, return True if any value
# appears at least twice in the array.
#
# Return False if every element is unique.
#
# Example 1:
# nums = [1, 2, 3, 1]
# Output: True
#
# Explanation:
# The number 1 appears more than once.
#
# Example 2:
# nums = [1, 2, 3, 4]
# Output: False
#
# Explanation:
# Every number appears only once.
#
# ---------------------------------------------------------
# Concept:
# ---------------------------------------------------------
# We use a SET because we only need to know whether a
# number has already appeared.
#
# Set stores unique values.
#
# Example:
#
# seen = set()
#
# seen.add(4)
# seen.add(7)
#
# seen = {4, 7}
#
# ---------------------------------------------------------
# Approach:
# ---------------------------------------------------------
# 1. Create an empty set called seen.
# 2. Loop through every number in nums.
# 3. Check whether the number is already in seen.
# 4. If it is already there, a duplicate exists.
# 5. Return True.
# 6. Otherwise, add the number to seen.
# 7. If the loop finishes without finding a duplicate,
#    return False.
#
# ---------------------------------------------------------
# Important Python:
# ---------------------------------------------------------
# Empty set:
# seen = set()
#
# Add a value:
# seen.add(num)
#
# Check whether a value exists:
# if num in seen:
#
# ---------------------------------------------------------
# Solution:
# ---------------------------------------------------------

class Solution:
    def containsDuplicate(self, nums):
        # Set to store numbers we have already seen
        seen = set()

        # Check every number in the array
        for num in nums:

            # If the number already exists,
            # we found a duplicate
            if num in seen:
                return True

            # Store the current number
            seen.add(num)

        # No duplicate was found
        return False


# ---------------------------------------------------------
# Example:
# ---------------------------------------------------------

solution = Solution()

nums = [4, 7, 2, 9, 4]

print(solution.containsDuplicate(nums))

# Output:
# True
#
# Because 4 appears twice.
#
# [4, 7, 2, 9, 4]
#  ↑           ↑
#  first       duplicate
#
# ---------------------------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(n)
# ---------------------------------------------------------
