from typing import List

numbers = [2,7,11,15]
target = 9

def twoSum(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) -1
    while left < right:
        if nums[left] + nums[right] < target:
            left += 1
        if nums[left] + nums[right] > target:
            right -= 1
        else: return [left+1, right+1]
    return [-1, -1]

print(twoSum(numbers, target))