# LeetCode: 3Sum
# Link: https://leetcode.com/problems/3sum/
#
# TODO: Implement your solution here.
#
# Suggested workflow:
# 1. Read the problem carefully.
# 2. Identify the pattern/data structure.
# 3. Write the brute-force idea first.
# 4. Optimize to meet the constraints.
# 5. Add your own test cases.
#
# Expected LeetCode signature can be copied from the problem page.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        track_dups = {}
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                for k in range(0, len(nums)):
                    if i != j and i != k and j != k and (nums[i] + nums[j] + nums[k] == 0):
                        l = sorted([nums[i], nums[j], nums[k]])
                        track_dups[" ".join(map(str, l))] = l
        
        return list(track_dups.values())
