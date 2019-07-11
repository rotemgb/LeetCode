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
