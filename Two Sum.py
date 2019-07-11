class Solution(object):
    
    def twoSum(self, nums, target):
        # Create Hash Table
        d = {}
        # looping through pairs of indecies and numbers
        for i, num in enumerate(nums):
            # create a new target to search in dictionary
            new_target = target - num
            # if not in dictionary, add to dictionary
            if new_target not in d:
                d.update( { num : i } )
            # if it is, we found pair of numbers
            else:
                return [d[new_target], i]
            
# Two Sum
# Level: Easy

# Description:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]
