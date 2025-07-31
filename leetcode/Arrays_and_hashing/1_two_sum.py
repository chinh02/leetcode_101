
from typing import List


nums = [2,7,11,15]
target = 9

def twoSum(nums: List[int], target: int) -> List[int]:
    dictionary = {}
    n = len(nums)
    for i in range(n):
        a = target - nums[i]
        if a in dictionary:
            return [dictionary[a], i]
        dictionary[nums[i]] = i

print(twoSum(nums,target))