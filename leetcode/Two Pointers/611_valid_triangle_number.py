# Given an integer array nums, 
# return the number of triplets chosen from the array that can make triangles 
# if we take them as side lengths of a triangle.

from typing import List


def triangleNumber(nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0
    result = 0
    nums.sort()
    for k in range(n-1,1,-1):
        i = 0
        j = k-1
        while i < k:
            if nums[i] + nums[j] > nums[k]:
                result += k - i
                k -= 1
            else:
                i += 1
    return result

nums = [4,2,3,4,5,6,7,2]
print(triangleNumber(nums))
