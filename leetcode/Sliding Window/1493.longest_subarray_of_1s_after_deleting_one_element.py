# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

nums = [0,1,1,1,0,1,1,0,1]

from typing import List

def longestSubarray(nums: List[int]) -> int:
        left = 0
        zeroes = 0
        best = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes >= 2:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            best = max(best, right - left + 1)
        return max(best-1, 0)

print(longestSubarray(nums))
